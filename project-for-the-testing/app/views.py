from django.shortcuts import render
from .models import *
from accounts.forms import *

from django.conf import settings
from django.urls import reverse_lazy

from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic.base import View

# Create your views here.

class HomeView(View):

	def get(self,request):
		return render(request, 'home.html')

# class HomeView(View):
# 	def get(self,request):
# 		form = NewsletterForm()
# 		news = News.objects.all()
# 		return render(request, 'home.html',{'form':form, 'news':news})
# 	def post(self, request):
# 		if request.method == 'POST':
# 			form = NewsletterForm(request.POST)
# 			if form.is_valid():
# 				data = form.save(commit=False)
# 				messages.add_message(request, messages.SUCCESS, 'Rahmat sizga ', data.get_name())
# 				send_mail(f'Hello - {data.get_name()}',
# 				'We send email to you!', settings.EMAIL_HOST_USER,[data]
# 				)
# 				form.save()
# 			return render(request, 'home.html', {'form':form})
# 		else:
# 			form = NewsletterForm()
# 			messages.add_message(request, messages.WARNING, 'NO NO NO')
#
# 		return render(request, 'home.html', {'form':form})



# from django.conf import settings
# msg = render_to_string('path\to\template.html', {'test_variable': 'xxx'})
# send_mail('Тема', msg , settings.EMAIL_HOST_USER, ['to@example.com']