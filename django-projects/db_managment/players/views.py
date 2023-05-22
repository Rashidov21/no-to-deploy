

from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse

from django.shortcuts import render, redirect
from django.views.generic import View, ListView,DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Player,Club

from django.db.models import Min, Max, Avg , Q, F

from django.core.mail import send_mail, send_mass_mail
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def players_sort_by_club(club_name):
    pass

class PlayersHomeView(LoginRequiredMixin,ListView,FormView):
    model = Player
    template_name = "players/players.html"
    form_class = UserCreationForm
    success_url = '/'
    # context_object_name = "object_list"
    
    def get_queryset(self):
        mun = Club.objects.get(name='Manchester United')
        qs = super().get_queryset()
        
        return qs.filter(club=mun.id)
    

        return total
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["club_list"] = Club.objects.all()
        return context
    
    



    
    # http get method handler 
    # def get(self,request):
        
        
        
    #     players = Player.objects.all()
    #     # for p in players:
    #     #     p.age = calculate_age(p.birthday)
    #     #     p.save()
    #     clubs = Club.objects.all()       

    #     data = {
    #         "object_list":players,
    #         "club_list":clubs,
    #     }
    #     return render(request, "players/players.html", context=data)
    
    # # http post method handler 
    # def post(self,request):
    #     pass

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

        
        
        
        if price or age:
            object_list= Player.objects.filter(
                Q(current_price__lte=int(price)) | Q(age__lte=int(age))
                )

           
            print(object_list)
            data = {
                "object_list":object_list,
                "info":f"Sorting players by filter form."
            }
            return render(request, "players/players.html", context=data)
        else:
            return render(request, "players/players.html")
        


def sort_by_club_and_positon(request):

    club = Club.objects.get(name=request.POST.get("country"))
    players = Player.objects.filter(
        Q(club=club.id) &  Q(position=request.POST.get("positon"))
    )
    clubs = Club.objects.all() 
    data = {
        "object_list":players,
        "club_list":clubs,
    }
    return render(request, "players/players.html", context=data)