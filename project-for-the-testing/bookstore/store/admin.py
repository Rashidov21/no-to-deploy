from django.contrib import admin
from .models import Category, Product
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    prepopulated_fields = {"slug": ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'in_stock']
    prepopulated_fields = {"slug": ('name',)}
