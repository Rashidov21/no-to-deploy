from django.shortcuts import render

# Create your views here.


class NotesView(ListView):
    model = Notes
