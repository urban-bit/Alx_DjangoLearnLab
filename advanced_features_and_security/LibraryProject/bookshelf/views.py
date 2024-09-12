from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

# View to display the list of books
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    View for listing all books.
    Permission required: can_view
    """
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})  # Render books in a template

# View to create a new book
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    """
    View for creating a new book.
    Permission required: can_create
    """
    # Logic for handling book creation (e.g., a form)
    # For now, we will return a simple template as a placeholder
    return render(request, 'bookshelf/book_create.html')

# View to edit an existing book
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    """
    View for editing an existing book.
    Permission required: can_edit
    """
    book = get_object_or_404(Book, id=book_id)  # Get the book or return a 404 error if not found
    return render(request, 'bookshelf/book_edit.html', {'book': book})

# View to delete a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    """
    View for deleting an existing book.
    Permission required: can_delete
    """
    book = get_object_or_404(Book, id=book_id)  # Get the book or return a 404 error if not found
    return render(request, 'bookshelf/book_delete.html', {'book': book})
