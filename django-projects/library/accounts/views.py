from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

# password reset views
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin


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
        if form.is_valid():
            user = form.save()
            # add user to group
            gp = Group.objects.get(name="users")
            user.groups.add(gp.id)
            user.save()
            # login new user
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


class CustomPasswordReset(PasswordResetView, SuccessMessageMixin):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.html'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')
