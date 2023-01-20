from django.contrib import admin
from .models import Category, Brand, Color, Product, ProductImages, Contact
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    prepopulated_fields = {"slug":("name",)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    prepopulated_fields = {"slug": ("name",)}
    
admin.site.register(Color)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "discount")
    list_filter = ("category", "brand", "top", "views")
    search_fields = ("brand", "name", "description")
    prepopulated_fields = {"slug":("name",)}

admin.site.register(ProductImages)
admin.site.register(Contact)