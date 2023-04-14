from django.contrib import admin

from django.utils.html import mark_safe

from .models import *
# Register your models here.

admin.site.register(Club)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['image_tag','name', 'country', 'club', 'position','current_price']
    list_filter = ['club','country']
    list_editable = ['current_price']
    list_display_links = ["name", "country"]
    list_per_page = 10
    readonly_fields = ['image_tag']
    
    def image_tag(self,obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')

    
    