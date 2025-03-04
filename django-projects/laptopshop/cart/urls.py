from django.urls import path 

from . import views 

app_name = 'cart'

urlpatterns = [
    path("", views.CartView.as_view(), name='cart'),
    path("add/", views.add_to_cart, name="add"),
    path("delete/<int:product_id>/<int:qty>", views.deleteItem, name="delete"),
]
