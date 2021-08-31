from django import forms 
from .models import EmailNews

class NewsletterForm(forms.ModelForm):

	class Meta:
		model = EmailNews
		fields = ('name', 'email')

