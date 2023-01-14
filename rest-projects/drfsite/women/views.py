from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView

# main models
from .models import Women
from .serializer import WomenSerializer

class WomenApiView(ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer