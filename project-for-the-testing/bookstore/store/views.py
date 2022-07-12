import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Product
# Create your views here.


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {"object_list": products})


def add_to_wishlist(request):
    request.session.modified = True
    data = json.loads(request.GET.get("data"))
    try:
        wishlist = request.session["wishlist"]
    except:
        request.session["wishlist"] = []
        wishlist = request.session["wishlist"]
    else:

        if data["product_id"] not in wishlist:
            wishlist.append(data["product_id"])
            return JsonResponse({"status": 200})
        else:
            return JsonResponse({"status": 400})
    return JsonResponse({"status": 404})
