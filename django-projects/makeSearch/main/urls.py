from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path("", views.searchPageView, name='search_page'),
    path("results/", views.resultPageView, name='result_page'),
]
