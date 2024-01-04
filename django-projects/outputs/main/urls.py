from django.urls import path,reverse_lazy
from django.contrib.auth import views as auth_views

from . import views

app_name = "main"

urlpatterns = [
    path("", auth_views.LoginView.as_view(template_name="login.html")),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="login.html"), name="logout"),
    path("register/", views.register, name="register"),

    path('password-reset/',auth_views.PasswordResetView.as_view(
        template_name='password-reset.html',
        html_email_template_name='password-reset-email.html',
        email_template_name='password-reset-email.html',
        success_url=reverse_lazy('main:password_reset_done')),
         name='password_reset' ),
    
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password-confirm.html',
        
         ),name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password-reset-form.html',
        success_url=reverse_lazy('main:password_reset_complete')),
         name='password_reset_confirm'),
    
      path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='register-success.html',
        
         ),name='password_reset_complete'),
]