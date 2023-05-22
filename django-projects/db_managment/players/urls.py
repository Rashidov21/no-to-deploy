from django.urls import path
from .import views

app_name = 'players'

urlpatterns = [
    path('', views.PlayersHomeView.as_view(), name='players'),
    path('detail/<pk>', views.PlayerDetailView.as_view(), name='player_detail'),
    
    # filtering and sort 
    path('sort/by/club/<str:club_name>', views.SortByClub.as_view(), name='sort_by_club'),
    path('sort/by/position/<str:position>', views.SortByPositon.as_view(), name='sort_by_position'),
    path("filter-form/", views.PlayerFilterFormView.as_view(), name='player_filter_form'),
    path('sort_by_club_and_positon/', views.sort_by_club_and_positon, name='sort_by_club_and_positon')
    
]

