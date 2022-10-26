from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=300)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images/')
    body = models.TextField()
    tag = models.ManyToManyField(Tag)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
