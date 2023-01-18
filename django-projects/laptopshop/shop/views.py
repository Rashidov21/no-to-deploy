from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from .models import Product


class HomePageView(View):
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        popular_products = Product.objects.filter(top=True)
        discount_products = Product.objects.filter(discount__gte=0)
        
        data = {
            "popular_products":popular_products,
            "discount_products":discount_products
        }
        
        return render(request, self.template_name, context=data)

