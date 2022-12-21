from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# Create your views here.


# def login(request):

#     username = request.POST.get("username")
#     password = request.POST.get("password")
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(user)
#         # Redirect to a success page.
#         return HttpResponse(f"Success !\n User is auth..{user.username} ")
#     else:
#         # Return an 'invalid login' error message.
#         return render(request, "accounts/login.html")
#     return render(request, "accounts/login.html")


def register(request):
    return render(request, "accounts/register.html")
