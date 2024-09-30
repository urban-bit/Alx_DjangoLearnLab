# api/views.py
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Add filter, search, and ordering capabilities
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Fields to filter by
    filterset_fields = ['title', 'author__name', 'publication_year']
    
    # Fields to search by
    search_fields = ['title', 'author__name']
    
    # Fields to order by
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering
