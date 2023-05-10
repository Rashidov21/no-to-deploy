from django.shortcuts import render
from django.views.generic.base import View
# from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import *

# Create your views here.


class HomePageView(View):
    
    
    def get(self,request):
        object_list = Product.objects.all()
        data = {
            "object_list":object_list
        }
        return render(request, 'index.html', context=data)
    
    def post(self,request):
        pass