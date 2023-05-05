from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg
# from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return str(self.name)
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return str(self.name)


  
class Article(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    tag = models.ManyToManyField(Tag, related_name="tags")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    body = models.TextField()
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)
    on_top = models.BooleanField(default=False)
    comments = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    
    @property
    def average_rating(self):
        rating = self.rating_set.all().aggregate(Avg('value'))['value__avg']
        if rating:
            return rating
        else:
            return 0 
    
    # def set_tags(self, tag_list):
    #     self.tag.add(*tag_list)
        # for tag in tag_list:
        #     self.tag.add(tag)
    
    def __str__(self):
        return str(self.title)

class Rating(models.Model):
    value = models.PositiveIntegerField(default=0)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='post_comments')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    comment = models.TextField()
    
    def __str__(self):
        return str(self.article.slug)
    
    
