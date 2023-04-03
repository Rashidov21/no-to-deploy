from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import messages

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
    article = Article.objects.select_related("author").get(slug=article_slug)  
    
    if check_article_view(request,article.id):
        article.views += 1
        article.save()
    else:
        pass  
    article_comments = article.post_comments.all()
    data = {"object":article, 'comments':article_comments}
    if request.method == "POST":
        comment = request.POST.get("comment")
        u = None
        if request.user.is_authenticated:
            u = request.user
        else:
            u = None
     
        
        if len(comment) > 3:
            Comment.objects.create(article=article, user=u,comment=comment)
            messages.add_message(request, messages.SUCCESS, "Commented !")
            data.update({"comments":article_comments})
            return render(request, 'articles/detail.html', context=data)
        else:
            messages.add_message(request, messages.WARNING, "Comment too short !")
            return render(request, 'articles/detail.html', context=data)
            
    return render(request, 'articles/detail.html', context=data)

def category_list(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    articles = Article.objects.filter(category=category)
    return render(request, 'articles/category_posts.html', context={"posts":articles})
    # comm
    
import json
def add_rating(request):
 
    data = json.loads(request.GET.get("data"))

    if data:
        article = Article.objects.get(pk=int(data.get("article_id")))
        for rate in article.rating_set.all():            
            if request.user == rate.user:
                return JsonResponse({"status":400})
        else:
            Rating.objects.create(
                value=int(data.get("rating")),
                article=article,
                user=request.user
            )
            return JsonResponse({"status":200, "updated_rating":article.average_rating})
    else:
        return JsonResponse({"status":404})
    

def delete_comment(request, comment_id):
    com = Comment.objects.get(pk=comment_id)
    com.delete()
    
    return redirect("/posts/detail/"+com.article.slug)
    