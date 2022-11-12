from django.shortcuts import render
from django.views.generic import ListView

from django.contrib.postgres.search import SearchQuery, SearchVector

from main.models import Player
# Create your views here.


def searchMethodView(request):
    q = request.GET.get("query")

    # obj = Player.objects.annotate(search=SearchVector("name", "club__name")).filter(
    #     search=q)
    # print(obj)
    return render(request, 'search.html')


class SearchClassView(ListView):
    model = Player
    template_name = 'search.html'
