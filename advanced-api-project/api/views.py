# api/views.py

from django_filters import rest_framework as filters  # Import django-filters for filtering
from rest_framework import generics  # Import generics for ListAPIView
from rest_framework import filters as rest_filters  # Import filters for search and ordering
from .models import Book  # Import your Book model
from .serializers import BookSerializer  # Import your Book serializer


# Define filter set for Book model to enable filtering by fields
class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact', 'icontains'],  # Filter books by exact title or partial match (case insensitive)
            'author__name': ['exact', 'icontains'],  # Filter by author name
            'publication_year': ['exact', 'gte', 'lte'],  # Filter by publication year (exact, greater than, less than)
        }


# Create the BookList view with filtering, searching, and ordering capabilities
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Queryset to retrieve all books
    serializer_class = BookSerializer  # Specify the serializer class
    filter_backends = [
        filters.DjangoFilterBackend,  # Enable filtering
        rest_filters.SearchFilter,  # Enable search functionality
        rest_filters.OrderingFilter,  # Enable ordering functionality
    ]
    filterset_class = BookFilter  # Specify the filterset for filtering fields
    search_fields = ['title', 'author__name']  # Enable searching by title and author name
    ordering_fields = ['title', 'publication_year']  # Allow ordering by title or publication year
    ordering = ['title']  # Default ordering is by title
