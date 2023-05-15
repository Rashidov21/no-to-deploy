from django.urls import path 
from . import views 


app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('add/<int:product_id>', views.AddToCartView.as_view(), name='add_to_cart')

]
