from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    published_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
