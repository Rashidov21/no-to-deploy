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
    
import json
def add_to_cart(request):
    data = json.loads(request.body)
    # print(data)
    cart = cart_init(request)
    status = cart.add(product_id=data.get("product_id"), qty=data.get("qty"))
    if status.get("done"):
        return JsonResponse({"status":"added"})
    else:
        return JsonResponse({"status":"notadded"})
    
def deleteItem(request,product_id,qty):
    cart = cart_init(request)
    cart.deleteItem(product_id,qty)
    return redirect('cart:cart')