from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Book)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]
    prepopulated_fields = {"slug": ("name",)}
