from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Book, Category


class BookListPageView(ListView):
    model = Book
    # template_name = 'index.html'


class BookDetailView(DetailView):
    model = Book


class CategoryListView(ListView):
    model = Category
    template_name = 'main/category_list.html'

    def get_queryset(self):
        if self.kwargs.get('slug'):
            category = self.model.objects.get(slug=self.kwargs.get('slug'))
            queryset = Book.objects.filter(category=category)
        return queryset

# CRUD Views


class CreateBookView(CreateView):
    # template_name = None
    # template_name_suffix = '_create'
    model = Book
    fields = ["title", "category", "poster", "description"]
    success_url = '/'


class UpdateBookView(UpdateView):
    # book_update_form.html
    template_name = 'main/book_form.html'
    model = Book
    fields = ["title", "category", "poster"]
    success_url = '/'


class DeleteBookView(DeleteView):
    model = Book
    success_url = '/'
