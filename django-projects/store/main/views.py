from django.shortcuts import render
from django.views.generic.base import View
# from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


class HomePageView(View):
    
    
    def get(self,request):
        return render(request, 'index.html')
    
    def post(self,request):
        pass