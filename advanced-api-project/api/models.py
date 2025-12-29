from django.db import models

# Author model represents a writer of books.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Book model represents a book written by an author.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    # Foreign Key linking to the Author model.
    # established a one-to-many relationship: One author can write multiple books.
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
