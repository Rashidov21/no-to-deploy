from django.db import models

# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=50)
    color_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Statuses"


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Categories"


class Notes(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Notes"
