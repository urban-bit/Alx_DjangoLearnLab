# Create Operation

## Command

```python
from bookshelf.models import Book  # Replace 'bookshelf' with your app name

# Create and save a new Book instance
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

