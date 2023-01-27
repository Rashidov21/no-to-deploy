from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class ProfileView(TemplateView):
    template_name = "account/profile.html"