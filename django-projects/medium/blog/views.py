from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Tag, Post

# Create your views here.


def homePageView(request):
    random_posts = Post.objects.all().order_by("?")[:4]  # 6 posts
    all_posts = Post.objects.all()

    paginator = Paginator(all_posts, 1)  # Show 3 posts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # print(page_obj)
    # print(dir(page_obj))
    data = {
        'random_posts': random_posts,
        'page_obj': page_obj
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


def search(request):
    q = request.GET.get('q')
    # contains - katta va kichik harflar inobatga olinadi
    # icontains - katta va kichik harflardan qatiy nazar mavjud bolsa olish
    # exact - aniq topish >> A2s
    # iexact - katta kichik harflardan qatiy nazar aniq topish
    # lte - teng yoki katta
    # gte - teng yoki kichik
    posts = Post.objects.filter(
        Q(title__icontains=q) | Q(body__icontains=q)
        # Q(author__iexact=q)
    )

    return render(request, 'results.html', context={"posts": posts})
