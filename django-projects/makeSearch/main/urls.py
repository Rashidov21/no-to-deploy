from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'main'

urlpatterns = [
    # Player add
    path("add/", views.ManagerAddView.as_view(), name='add'),
    path("managers/", views.ManagersView.as_view(), name='managers'),
    # TemplateView() variant 1
    path("", views.IndexTemplateView.as_view(), name='home'),
    # TemplateView() variant 2
    path("template-2/", TemplateView.as_view(template_name='index.html')),
    # listview
    path("list/players/", views.PlayerListView.as_view(), name='player_list'),
    path("search/", views.searchPageView, name='search_page'),

    # search results page
    path("results/", views.resultPageView, name='result_page'),
    # inline search
    path("inline/search/", views.inlineSearch, name='inline_search')
]
