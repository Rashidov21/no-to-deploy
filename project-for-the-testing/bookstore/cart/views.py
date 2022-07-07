from django.shortcuts import render, redirect
from store.models import Product
# from django.http import re
from .models import Cart
# Create your views here.


def cart_init(request):
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create()
        request.session['user_cart_id'] = cart.id
    return cart


def cart_view(request):
    cart = cart_init(request)

    return render(request, 'cart.html', {'cart': cart})


def addToCart(request, product_id):

    cart = cart_init(request)
    cart.add(product_id, 1)
    return redirect("cart:cart")
