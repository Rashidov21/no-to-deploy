from django.forms import ModelForm
from .models import Book

# Add new book form


class AddBookForm(ModelForm):

    class Meta:
        model = Book
        fields = ["title", "category", "poster"]
        exclude = ["views"]
        widgets = None
