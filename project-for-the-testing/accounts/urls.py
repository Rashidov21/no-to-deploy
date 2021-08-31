from django.urls import path
from . import views



app_name = 'accounts'

urlpatterns = [
	path('login/', views.AppLoginView.as_view(), name='app_login') ,
	path('logout/', views.AppLogoutView.as_view() ,name='app_logout'), 
	path('register/', views.register, name='register'),
	path('profile/', views.profile, name='user_profile'),
]