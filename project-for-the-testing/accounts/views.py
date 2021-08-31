from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from .models import *
from .forms import *

from django.conf import settings
from django.urls import reverse_lazy

from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from django.contrib.auth.views import LoginView

class AppLoginView(LoginView):
	template_name='accounts/login.html'



class AppLogoutView(LoginRequiredMixin,LogoutView):
	template_name = 'accounts/logout.html'

@login_required
def profile(request):
	pw = len(request.user.username)
	chars = pw * '*'

	print(type(chars))
	return render(request, 'accounts/profile.html',{'password':chars})


def register(request):
	return render(request, 'accounts/register.html')