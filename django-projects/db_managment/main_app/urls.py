from django.urls import path
from .import views

app_name = 'main_app'

urlpatterns = [
    path('', views.testView, name='test'),
    path('search/', views.search, name='search'),
    path('add/course/', views.add_course_view, name="add_course")
]

