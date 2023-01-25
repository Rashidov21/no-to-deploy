from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import JsonResponse
# Create your views here.

from shop.models import Product
from .models import Cart

# request.session - sessiya >> dict >> user saytga kirib to chiqib ketguniga qadar bo'lgan vaqt (ma'lumotlat) 

# print(request.session)

def cart_init(request):
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create() # yangi cart object hosil qilish
        request.session['user_cart_id'] = cart.id
    return cart


class CartView(TemplateView):
    template_name = "shopping.html"
    
    def get(self, request):
        # print(type(request.session))
        # print(dir(request.session))
        cart = cart_init(request)
        return render(request, self.template_name, {"cart":cart})
    

def add_to_cart(request):
    print(request.POST)

    
    return JsonResponse({"status":200})