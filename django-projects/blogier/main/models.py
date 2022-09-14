from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    """Post model"""
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=50)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    # Relation
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
