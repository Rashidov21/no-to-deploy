from django.shortcuts import render
from .models import Player

from django.db.models import Q
# Create your views here.


def searchPageView(request):
    players = Player.objects.all()

    data = {
        "players": players
    }
    return render(request, "index.html", context=data)


def resultPageView(request):
    q = request.GET.get("query")
    # print(type(q))
    if len(q) >= 3:
        # query = Player.objects.filter(name__icontains=q)
        query = Player.objects.filter(
            Q(name__icontains=q) | Q(club__name__icontains=q) | Q(
                country__name__icontains=q)
        )
        return render(request, "result.html", {"object_list": query})
    return render(request, "result.html")
