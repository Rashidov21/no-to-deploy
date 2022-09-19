from django.urls import path
from .import views

app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('detail/<slug:post_slug>',
         views.post_detail, name='detail'),
    path('category/<slug:category_slug>',
         views.category_list, name='category_list'),
]
