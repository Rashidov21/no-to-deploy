from django.urls import path 
from . import views 


app_name = 'main'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path("category/<slug>", views.CategoryListView.as_view(), name='category_list'),
    
    path('results/', views.SearchListView.as_view(), name='search')
]
