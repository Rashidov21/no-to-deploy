from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
# from .forms import CreateUserForm


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Well done !")
            return redirect("/")
        else:
            messages.add_message(request, messages.WARNING,
                                 "Something went wrong !")
    else:

        return render(request, "accounts/register.html", {"form": form})
    return render(request, "accounts/register.html", {"form": form})
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
