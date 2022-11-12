from django.urls import path
from . import views
app_name = 'search'

urlpatterns = [
    path('', views.searchMethodView, name='search_method'),
    path('withclass/', views.SearchClassView.as_view(), name='search_class'),
]
