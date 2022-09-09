from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('', views.homePage, name='home'),
    path('contact/', views.contactPage,
         name='contact'),
    path('user/<int:id>/<str:username>',
         views.userPage, name='userprofile')
]
