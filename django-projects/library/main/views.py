from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Book, Category, Author


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
