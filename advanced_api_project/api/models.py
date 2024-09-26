# api/models.py

class Author(models.Model):
    """
    The Author model represents a writer of books.
    An author can have multiple books associated with them.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    The Book model stores information about individual books.
    Each book is linked to an author through a ForeignKey relationship.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
