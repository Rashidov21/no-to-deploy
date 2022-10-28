from django.contrib import admin
from .models import Player
# Register your models here.


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'country']
    list_display_links = ["name"]
    list_filter = ["club", "position"]
