# relationship_app/urls.py

from django.urls import path
from .views import list_books, BookListView

urlpatterns = [
    # URL pattern for the function-based view
    path('books/', list_books, name='list_books'),

    # URL pattern for the class-based view
    path('books/class/', BookListView.as_view(), name='book_list_class'),

    # You can add more URL patterns here as needed
]
