from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class PlayersHomeView(View):
    
    
    # http get method handler 
    def get(self,request):
        return render(request, "players/players.html")
    
    # http post method handler 
    def post(self,request):
        pass