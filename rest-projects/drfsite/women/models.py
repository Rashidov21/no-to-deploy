from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    
    def __str__(self):
        return str(self.name)

class Women(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return str(self.title)