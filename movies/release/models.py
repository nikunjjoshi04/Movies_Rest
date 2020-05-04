from django.db import models

# Create your models here.


# Movie Model
class Book(models.Model):
    name = models.CharField(max_length=100)
    genres = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Cast Model
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


# Release Model
class Release(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    release_data = models.DateField()
    authors = models.ManyToManyField(Author)
    ratings = models.IntegerField()

    def __str__(self):
        return '{} -- {}'.format(self.book, self.ratings)
