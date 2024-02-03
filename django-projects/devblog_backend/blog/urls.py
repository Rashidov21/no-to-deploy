from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("",views.post_list, name='post_list')
]


arr = [1,2,3,4,5]

for i in range(500):
    arr.append(i)
    
l = list(range(500))

l = list( range(2,500,2) )