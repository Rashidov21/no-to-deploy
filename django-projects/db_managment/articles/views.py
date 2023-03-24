from django.shortcuts import render

# Create your views here.
def all_articles_view(request):
    return render(request, "articles/posts.html")