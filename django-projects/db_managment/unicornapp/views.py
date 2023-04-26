from django.shortcuts import render

# Create your views here.

def index(request):
    context = {"form": {}}
    return render(request, "reactive-app/index.html", context)