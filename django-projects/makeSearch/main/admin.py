from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['club__name', 'country__name']


@admin.register(ClubManager)
class ClubManagerAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['club__name', 'country__name']
