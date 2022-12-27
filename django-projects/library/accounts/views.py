from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib import messages
# Create your views here.
from .models import User
from .forms import CreateUserForm


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
  
        form = CreateUserForm(request.POST)
        for i in form:
            print(i)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Well done !")
            return redirect("/")
        else:
            messages.add_message(request, messages.WARNING,
                                 "Something went wrong !")
    else:

        return render(request, "accounts/register.html", {"form": form})
    return render(request, "accounts/register.html", {"form": form})


class ProfileEditView(UpdateView):
    model = User
    fields = ["first_name", "last_name", "photo", "gender", "age", "bio"]
    success_url = "/accounts/profile"


class OtherProfileView(DetailView):
    model = User
