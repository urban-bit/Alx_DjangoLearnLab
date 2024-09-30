# api/test_views.py

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Book, Author
from .serializers import BookSerializer

class BookAPITestCase(APITestCase):
    
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Create a sample author and books to use for testing
        self.author = Author.objects.create(name='Author 1')
        self.book1 = Book.objects.create(title='Test Book 1', publication_year=2000, author=self.author)
        self.book2 = Book.objects.create(title='Another Book', publication_year=2010, author=self.author)

    # Test: List all books
    def test_list_books(self):
        url = reverse('book-list')  # URL for listing books
        response = self.client.get(url)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    # Test: Retrieve single book
    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # Test: Create a new book
    def test_create_book(self):
        url = reverse('book-list')
        data = {
            'title': 'New Book',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'New Book')

    # Test: Update an existing book
    def test_update_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        data = {
            'title': 'Updated Book Title',
            'publication_year': self.book1.publication_year,
            'author': self.book1.author.id
        }
        response = self.client.put(url, data, format='json')
        self.book1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.book1.title, 'Updated Book Title')

    # Test: Delete a book
    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # Test: Filter books by title
    def test_filter_books_by_title(self):
        url = reverse('book-list') + '?title=Test Book 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book 1')

    # Test: Search books by author name
    def test_search_books_by_author_name(self):
        url = reverse('book-list') + '?search=Author 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # Test: Ordering books by publication year
    def test_order_books_by_publication_year(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Book 1')  # 2000 is earlier than 2010
