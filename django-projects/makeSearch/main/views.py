from django.shortcuts import render

# Create your views here.


def searchPageView(request):
    return render(request, "index.html")


def resultPageView(request):
    return render(request, "results.html")
