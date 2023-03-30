from django.shortcuts import render

from .models import *
from .utils import check_article_view

# Create your views here.
def all_articles_view(request):
    # request.session.clear()
    # print(request.session.get("read_articles"))
    
    
    
    all_categories = Category.objects.all()
    all_posts = Article.objects.all()
    
    data = {
        'posts':all_posts,
        'categories':all_categories
    }
    
    return render(request, "articles/posts.html", context=data)





def post_detail(request,article_slug):
    article = Article.objects.get(slug=article_slug)  
    
    if check_article_view(request,article.id):
        article.views += 1
        article.save()
    else:
        pass  

    return render(request, 'articles/detail.html', context={"object":article})

def category_list(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    articles = Article.objects.filter(category=category)
    return render(request, 'articles/category_posts.html', context={"posts":articles})
    # comm
    