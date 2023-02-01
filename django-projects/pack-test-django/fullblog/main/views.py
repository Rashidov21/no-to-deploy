from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from .models import Musician

class HomePageView(ListView):
    model = Musician
    template_name = 'index.html'