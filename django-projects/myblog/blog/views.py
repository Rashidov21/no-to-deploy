from django.shortcuts import render
from .models import Post
# Create your views here.


def home_page(request):
    all_posts = Post.objects.all()
    context = {
        'posts': all_posts
    }
    return render(request, 'index.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post-detail.html', {"post": post})
