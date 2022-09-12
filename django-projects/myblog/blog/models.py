from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(verbose_name='Maqola nomi', max_length=250)
    body = models.TextField(verbose_name='Maqola matni')
    image = models.ImageField(upload_to='post_images/%Y/%M/%D')
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
