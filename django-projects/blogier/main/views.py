from django.shortcuts import render
from .models import Category, Post
# Create your views here.


def home(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    context = {
        "categories": categories,
        "posts": posts
    }
    return render(request, 'index.html', context)
