from bookshelf.models import Book  # Ensure this import is correct

# Retrieve the book instance to be deleted
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book instance
book.delete()

# Confirm deletion by retrieving all books
books = Book.objects.all()
print(books)  # This should be an empty QuerySet
