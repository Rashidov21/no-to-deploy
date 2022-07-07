from django.contrib import admin
from .models import CardProduct, Cart
# Register your models here.


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_quantity', 'total_price']


@admin.register(CardProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'price']
