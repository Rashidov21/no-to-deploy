from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
# Create your views here.
from .models import Notes, Category, Status


class NotesView(ListView):
    """all notes view"""
    model = Notes


class AddNoteView(View):
    """One note view"""
    template_name = 'add.html'

    def get(self, request, *args, **kwargs):
        form = AddNoteForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):

        if request.method == "POST":
            form = AddNoteForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("/")
        else:
            render(request, self.template_name)
        return render(request, self.template_name, {"form": form})
