from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.core.exceptions import ValidationError


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email"]

        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            # "password": forms.PasswordInput(attrs={"class": "form-control"})
            # "last_name": forms.CharField(attrs={"class": "form-control"})
        }

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2
