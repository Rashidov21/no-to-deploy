from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name="Kategoriya nomi", max_length=100)

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    title = models.CharField(verbose_name="Maqola nomi", max_length=350)
    body = models.TextField()
    author = models.CharField(verbose_name="Maqola muallifi", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Foydalanuvchi ismi", max_length=100)
    comment = models.TextField()

    def __str__(self):
        return str(self.post.title)
