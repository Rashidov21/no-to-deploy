from django.db import models

# Create your models here.
class BannerAd(models.Model):
    image = models.ImageField(upload_to='banners/')
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    link = models.URLField()
    
    class Meta:
        verbose_name_plural = "Banners"
        
    def __str__(self):
        return str(self.title)
    
class Category(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    image = models.ImageField(upload_to='categories/')
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return str(self.title)
    
    
class Food(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='foods/')
    price = models.PositiveIntegerField(default=0)
    stars = models.PositiveSmallIntegerField(default=0)
    discount = models.PositiveSmallIntegerField(default=0)
    
    class Meta:
        verbose_name_plural = "Foods"
        
    def __str__(self):
        return str(self.name)
    