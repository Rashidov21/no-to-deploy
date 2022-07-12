import json
from django.shortcuts import render, redirect
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


def wishlist(request):
    try:
        wishlist = request.session["wishlist"]
    except:
        request.session["wishlist"] = []
        wishlist = request.session["wishlist"]
    else:
        obj_list = []
        for obj_id in wishlist:
            p = Product.objects.get(id=obj_id)
            obj_list.append({"product": p})

    return render(request, "wishlist.html", {"object_list": obj_list})


def deleteFromWishlist(request, pr_id):
    request.session.modified = True
    wishlist = request.session["wishlist"]
    print(wishlist)
    if wishlist:
        wishlist.remove(pr_id)
    return redirect("/wishlist/")
