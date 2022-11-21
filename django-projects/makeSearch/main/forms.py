from django.forms import ModelForm
from .models import ClubManager


class ManagerAddForm(ModelForm):

    class Meta:
        model = ClubManager
        fields = "__all__"
