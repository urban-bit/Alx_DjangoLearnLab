# relationship_app/urls.py

from django.urls import path
from .views import list_books, BookListView, LibraryDetailView

urlpatterns = [
    # URL pattern for the function-based view
    path('books/', list_books, name='list_books'),

    # URL pattern for the class-based view
    path('books/class/', BookListView.as_view(), name='book_list_class'),

    # URL pattern for the LibraryDetailView
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Add more URL patterns as needed
]
