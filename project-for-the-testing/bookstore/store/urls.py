
from django.urls import path
from .import views
app_name = 'store'
urlpatterns = [
    path("", views.home, name='home'),
    path("add_to_wishlist/",
         views.add_to_wishlist, name='add_to_wishlist'),
    path("wishlist/", views.wishlist, name='wishlist'),
    path("delete/<int:pr_id>", views.deleteFromWishlist, name='deleteFromWishlist'),
]
