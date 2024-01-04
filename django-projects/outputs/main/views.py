from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        if pass1 == pass2:
            u = User.objects.create(username=username, password=pass1)
            user = authenticate(request, username=u.username, password=u.password)
            if user is not None:
                login(request, user)
            return redirect("/")
    return render(request, "register.html")