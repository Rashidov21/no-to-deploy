from django.contrib import admin
from .models import Course, Student
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {"slug": ("name",)}


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'course']
    list_filter = ['course', 'age']
    prepopulated_fields = {"slug": ("name", "surname")}
