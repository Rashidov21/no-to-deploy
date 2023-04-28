from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.my_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),

]

