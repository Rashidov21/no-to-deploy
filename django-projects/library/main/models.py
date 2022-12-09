from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)


class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0, blank=True, null=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)
    views = models.PositiveIntegerField(default=0)
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return str(self.title)
