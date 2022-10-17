from django.urls import path
from . import views

app_name = 'main'


urlpatterns = [
    path("", views.home, name='home'),
    path("results/<int:quest_id>", views.results, name='results'),
    path("contact/", views.contact, name='contact'),
]
