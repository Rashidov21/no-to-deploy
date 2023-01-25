from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

from shop.models import Product

class CartView(TemplateView):
    template_name = "shopping.html"