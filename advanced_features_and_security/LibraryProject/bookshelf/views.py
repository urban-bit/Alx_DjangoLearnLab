from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

# View to display the list of books
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    View for listing all books.
    Permission required: can_view
    """
    books = Book.objects.all()  # Fetch all books using Django's ORM
    return render(request, 'bookshelf/book_list.html', {'books': books})  # Render books in a template

# View to create a new book
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    """
    View for creating a new book.
    Permission required: can_create
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)  # Use the form to handle book creation
        if form.is_valid():
            # Here you would process the data and save the new book instance
            return redirect('book_list')  # Redirect to the book list after successful creation
    else:
        form = ExampleForm()
    
    return render(request, 'bookshelf/book_create.html', {'form': form})

# View to edit an existing book
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    """
    View for editing an existing book.
    Permission required: can_edit
    """
    book = get_object_or_404(Book, id=book_id)  # Get the book or return a 404 if not found
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form and save changes
            return redirect('book_list')
    else:
        form = ExampleForm(initial={'name': book.title, 'email': 'author@example.com'})  # Populate form with book data

    return render(request, 'bookshelf/book_edit.html', {'form': form, 'book': book})

# View to delete a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    """
    View for deleting an existing book.
    Permission required: can_delete
    """
    book = get_object_or_404(Book, id=book_id)  # Get the book or return a 404 if not found
    if request.method == 'POST':
        book.delete()  # Delete the book
        return redirect('book_list')  # Redirect to the book list after deletion
    
    return render(request, 'bookshelf/book_delete.html', {'book': book})

# Example view using ExampleForm for demonstration
def example_view(request):
    """
    View to handle the ExampleForm.
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data, e.g., save the form data or send an email
            return redirect('success_view')  # Redirect to a success page
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/example_form.html', {'form': form})
