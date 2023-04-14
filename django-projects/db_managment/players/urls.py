from django.urls import path
from .import views

app_name = 'players'

urlpatterns = [
    path('', views.PlayersHomeView.as_view(), name='players'),
]

