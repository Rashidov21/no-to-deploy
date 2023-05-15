
from django.shortcuts import render
from django.views.generic.base import View 
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.db.models import Q

from .models import *

# Create your views here.


class HomePageView(View):
    
    
    def get(self,request):
        object_list = Product.objects.all()
        categories = Category.objects.all()
        data = {
            "object_list":object_list,
            "categories":categories
        }
        return render(request, 'index.html', context=data)
    
    def post(self,request):
        pass

class CategoryListView(ListView):
    model = Product
    template_name = 'list.html'


    
    def get_queryset(self):        
        slug = self.kwargs.get("slug")
        category  = Category.objects.get(slug=slug)
        qs = Product.objects.filter(category=category)
        return qs
    

class SearchListView(ListView):
    model = Product
    template_name = 'list.html'
    
    def get_queryset(self):
        qs = Product.objects.filter(
            Q(name__icontains=self.request.GET.get("query")) | Q(description__icontains=self.request.GET.get("query"))
        )
        return qs