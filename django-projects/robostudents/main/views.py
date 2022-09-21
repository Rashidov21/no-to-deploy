from django.shortcuts import render

# Create your views here.


def all_students(request):
    return render(request, "index.html")
