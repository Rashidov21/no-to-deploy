from django.urls import path 
from .import views 

app_name = 'articles'


urlpatterns = [
    path("", views.all_articles_view, name='post_list'),
    path('detail/<slug:article_slug>', views.post_detail, name='detail'),
    path("category/<slug:category_slug>/", views.category_list, name='category_list')
]
