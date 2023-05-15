from django.shortcuts import render, redirect
from django.views.generic.base import View

# Create your views here.
from .models import Cart

def cart_init(request):
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create() # yangi cart object hosil qilish
        request.session['user_cart_id'] = cart.id
    return cart


class CartView(View):
    
    def get(self, request):
        cart = cart_init(request)
        
        return render(request, 'cart.html', {"cart":cart})

class AddToCartView(View):
    
    def get(self, request, product_id):
        cart = cart_init(request)
        if cart:
            cart.add(product_id)
            return redirect('/')
        
        return render(request, 'cart.html', {"cart":cart})