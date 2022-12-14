from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, null=True)
    views = models.PositiveIntegerField(default=0, blank=True)
    poster = models.ImageField(upload_to='posters/')
    description = RichTextField()

    def __str__(self):
        return str(self.title)
