from django.db import models

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100) # Author's name

    def __str__(self):
        return self.name

# Book model
class Book(models.Model):
    title = models.CharField(max_length=200) # Book title
    publication_year = models.IntegerField() # Publication year of the book
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE) # Link to Author

    def __str__(self):
        return self.title