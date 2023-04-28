from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout

# Create your views here.

def my_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
    

    
        user = authenticate(request,username=username, password=password)
      
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            print("OK")    
            return redirect('/accounts/profile/')
        else:
            # No backend authenticated the credentials
            print("error")
            return render(request, "accounts/login.html")
    return render(request, "accounts/login.html")
           

        


def logout(request):
    pass
def profile(request):
    return render(request, "accounts/profile.html")