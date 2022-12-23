from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .import views

app_name = 'accounts'

urlpatterns = [
    path("register/", views.register, name='register'),
    # path("login/", views.login, name='login'),
    path("login/", LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path("logout/", LogoutView.as_view(template_name='accounts/login.html'), name='logout'),
    path("profile/", TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
]
