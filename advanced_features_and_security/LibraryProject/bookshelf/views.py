from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book
from .forms import BookForm  # Assuming you have a form for Book in forms.py

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
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new book to the database
            return redirect('book_list')  # Redirect to the book list after creation
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_create.html', {'form': form})

# View to edit an existing book
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    """
    View for editing an existing book.
    Permission required: can_edit
    """
    book = get_object_or_404(Book, id=book_id)  # Get the book or return a 404 error if not found

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # Save the changes to the book
            return redirect('book_list')  # Redirect to the book list after editing
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_edit.html', {'form': form, 'book': book})

# View to delete a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    """
    View for deleting an existing book.
    Permission required: can_delete
    """
    book = get_object_or_404(Book, id=book_id)  # Get the book or return a 404 error if not found

    if request.method == 'POST':  # Check if the request is a POST request (for delete confirmation)
        book.delete()  # Delete the book
        return redirect('book_list')  # Redirect to the book list after deletion
    return render(request, 'bookshelf/book_delete.html', {'book': book})
