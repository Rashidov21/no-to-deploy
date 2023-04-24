from datetime import date

from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Player,Club

from django.db.models import Min, Max, Avg 

# Create your views here.
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))



class PlayersHomeView(View):
    
    
    # http get method handler 
    def get(self,request):
        players = Player.objects.all()
        clubs = Club.objects.all()

        for pl in players:
            print(calculate_age(pl.birthday))

        

        data = {
            "object_list":players,
            "club_list":clubs,
        }
        return render(request, "players/players.html", context=data)
    
    # http post method handler 
    def post(self,request):
        pass

class SortByClub(View):
    
    def get(self,request,club_name):
        print(club_name)
        club = Club.objects.get(name=club_name)
        players = Player.objects.filter(club=club)
        
        clubs = Club.objects.all()
        data = {
            "object_list":players,
             "club_list":clubs,
             "info":f"Sorting players by club : {club_name}"
        }
        return render(request, "players/players.html", context=data)
        
    
class SortByPositon(View):
    
    def get(self,request,position):

        players = Player.objects.filter(position=position)
        
        clubs = Club.objects.all()
        data = {
            "object_list":players,
             "club_list":clubs,
             "info":f"Sorting players by postion."
        }
        return render(request, "players/players.html", context=data)
        
    