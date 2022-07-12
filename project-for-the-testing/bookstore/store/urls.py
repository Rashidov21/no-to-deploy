
from django.urls import path
from .import views
app_name = 'store'
urlpatterns = [
    path("", views.home, name='home'),
    path("wishlist/",
         views.add_to_wishlist, name='add_to_wishlist')
]
