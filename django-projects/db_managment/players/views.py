

from django.urls import reverse

from django.shortcuts import render
from django.views.generic import View, ListView,DetailView
from .models import Player,Club

from django.db.models import Min, Max, Avg , Q, F

# Create your views here.



class PlayersHomeView(View):
    
    
    # http get method handler 
    def get(self,request):
        
        
        
        players = Player.objects.all()
        # for p in players:
        #     p.age = calculate_age(p.birthday)
        #     p.save()
        clubs = Club.objects.all()       

        data = {
            "object_list":players,
            "club_list":clubs,
        }
        return render(request, "players/players.html", context=data)
    
    # http post method handler 
    def post(self,request):
        pass

class PlayerDetailView(DetailView):
    model = Player
    template_name = "players/player_detail.html"

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

class PlayerFilterFormView(View):
    
    
    def get(self,request):
        price = request.GET.get("price")
        age = request.GET.get("age")
        gk = request.GET.get("gk")
        df = request.GET.get("df")
        md = request.GET.get("md")
        fw = request.GET.get("fw")
        st = request.GET.get("st")
        
        
        
        if price or age or any([gk,df,md,fw,st]):
            object_list= Player.objects.filter(
               ( Q(position=gk) | Q(position=df) | Q(position=md)| Q(position=fw)| Q(position=st))
                ).filter(Q(current_price__lte=int(price)) | Q(age__lte=int(age)))

           
            print(object_list)
            data = {
                "object_list":object_list,
                "info":f"Sorting players by filter form."
            }
            return render(request, "players/players.html", context=data)
        else:
            return render(request, "players/players.html")
        


