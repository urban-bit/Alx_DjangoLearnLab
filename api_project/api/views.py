# api/views.py
from rest_framework import viewsets
from .models import Book  # Import your Book model
from .serializers import BookSerializer  # Import your Book serializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Queryset to retrieve all books
    serializer_class = BookSerializer  # Specify the serializer class
