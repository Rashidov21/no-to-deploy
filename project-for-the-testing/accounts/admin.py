from django.contrib import admin
from .models import AdvUser, EmailNews

# Register your models here.
@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
	list_display = ['id', 'username', 'first_name']
	list_display_links = ['username']

@admin.register(EmailNews)
class EmailNewsAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'email']