from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homePage(request):
    return render(request, 'index.html')


def contactPage(request):
    return render(request, 'contact.html')


def userPage(request, id, username):
    data = f"<h3>ID = {id} username = {username}</h3>"
    return HttpResponse(data)
