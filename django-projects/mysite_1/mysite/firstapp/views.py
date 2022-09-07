from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    print(request)
    print(request.path)
    print(request.method)
    print(dir(request))
    return HttpResponse("<h1>Its working ...</h1>")
