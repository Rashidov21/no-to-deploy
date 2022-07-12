import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Product
# Create your views here.


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {"object_list": products})


def add_to_wishlist(request):
    data = json.loads(request.GET.get("data"))
    print(data)
    return JsonResponse({"status": 200})
