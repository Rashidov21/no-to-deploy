from django import forms
from . models import Notes


class AddNoteForm(forms.ModelForm):
    """Add new Note Form"""

    class Meta:
        model = Notes
        fields = "__all__"
