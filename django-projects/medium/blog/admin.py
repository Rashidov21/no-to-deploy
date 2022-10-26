from django.contrib import admin
from . models import Tag, Post
# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ["name", 'slug']
    prepopulated_fields = {"slug": ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    list_display_links = ["title", 'author']
    prepopulated_fields = {"slug": ('title',)}
