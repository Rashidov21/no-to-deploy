from django.urls import path 
from .import views

app_name = 'shop'

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path("product/<slug>", views.ProductDetailView.as_view(), name='detail')
]
