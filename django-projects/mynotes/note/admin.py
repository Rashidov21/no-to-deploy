from django.contrib import admin
from .models import Status, Category, Notes
# Register your models here.


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Notes)
