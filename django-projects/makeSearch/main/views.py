from django.shortcuts import render
from .models import Player
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
        query = Player.objects.filter(name__icontains=q)
        return render(request, "result.html", {"object_list": query})
    return render(request, "result.html")
