from django.shortcuts import render
from django.views.generic import DetailView
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


class ProductDetailView(DetailView):
    template_name = "about.html"
    model = Product
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_products"] = self.object.tags.similar_objects()[:4]
        return context
