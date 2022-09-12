from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('detail/<int:post_id>', views.post_detail, name='post_detail')
]
