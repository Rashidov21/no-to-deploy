from django.shortcuts import render
from .models import Category, Post
from .forms import ContactForm
# Create your views here.


def home(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    context = {
        "categories": categories,
        "posts": posts
    }
    return render(request, 'index.html', context)


def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {"form": form})


def post_detail(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    return render(request, 'detail.html',
                  {"post": post})


def category_list(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category=category)
    return render(request, 'list.html', {"posts": posts})
