from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# class CreateUserForm(UserCreationForm):
#     password1 = forms.PasswordInput()
#     password2 = forms.PasswordInput()

#     class Meta:
#         model = User
#         fields = ["username", "first_name",
#                   "last_name", "password1", "password2"]
#         # exclude = ["is_staff", "is_superuser"]
#         widgets = {
#             "first_name": forms.CharField(attrs={"class": "form-control"}),
#             "last_name": forms.CharField(attrs={"class": "form-control"})
#         }

#     def clean_password2(self):
#         password1 = self.cleaned_data['password1']
#         password2 = self.cleaned_data['password2']

#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Password don't match")
#         return password2
