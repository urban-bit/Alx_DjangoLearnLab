from django.contrib import admin
from bookshelf.models import Book  # Import the Book model

# Define a custom admin class to customize the admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display these fields in the list view
    search_fields = ('title', 'author')  # Add search functionality for these fields
    list_filter = ('publication_year',)  # Add a filter sidebar for publication_year

# Register the Book model with the admin site using the custom admin class
admin.site.register(Book, BookAdmin)
