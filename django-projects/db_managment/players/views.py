from django.shortcuts import render
from django.views.generic import View
from .models import Player



# Create your views here.
class PlayersHomeView(View):
    
    
    # http get method handler 
    def get(self,request):
        players = Player.objects.all()
        data = {
            "object_list":players
        }
        return render(request, "players/players.html", context=data)
    
    # http post method handler 
    def post(self,request):
        pass