from django.shortcuts import render
from .models import Tag, Post

# Create your views here.


def homePageView(request):
    random_posts = Post.objects.all().order_by("?")[:4]  # 6 posts
    all_posts = Post.objects.all()
    data = {
        'random_posts': random_posts,
        'all_posts': all_posts
    }
    return render(request, 'index.html', context=data)


def postDetailView(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    related_posts = Post.objects.filter(tag=post.tag.all()[0])
    data = {
        "post": post,
        "related_posts": related_posts
    }
    return render(request, 'post.html', context=data)
