from django.shortcuts import render
from .models import Player
# Create your views here.


def homePageView(request):
    numbers = list(range(10))
    first_player = Player.objects.first()
    last_player = Player.objects.last()
    data = {
        'fp': first_player,
        'lp': last_player
    }
    # print(type(Player))
    # print(dir(Player))
    # objects - menejer - boshqaruvchi

    return render(request, "index.html", context=data)
