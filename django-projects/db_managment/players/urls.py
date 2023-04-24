from django.urls import path
from .import views

app_name = 'players'

urlpatterns = [
    path('', views.PlayersHomeView.as_view(), name='players'),
    
    # filtering and sort 
    path('sort/by/club/<str:club_name>', views.SortByClub.as_view(), name='sort_by_club'),
    path('sort/by/position/<str:position>', views.SortByPositon.as_view(), name='sort_by_position'),
    
]

