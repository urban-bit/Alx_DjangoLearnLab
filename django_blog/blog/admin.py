from django.contrib import admin
from .models import Post  # Import your Post model

# Create a custom admin class to manage the Post model
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')  # Fields to display in the list view
    list_filter = ('author', 'published_date')  # Filters for the list view
    search_fields = ('title', 'content')  # Searchable fields
    prepopulated_fields = {'slug': ('title',)}  # Automatically populate slug field from title

# Register the Post model with the custom admin class
admin.site.register(Post, PostAdmin)
