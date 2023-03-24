from django.urls import path 
from .import views 

app_name = 'articles'


urlpatterns = [
    path("", views.all_articles_view, name='post_list')
]
