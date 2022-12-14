from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path("", views.BookListPageView.as_view(), name='home'),
    path("detail/<int:pk>/", views.BookDetailView.as_view(), name='book_detail'),
    path('category/<slug:slug>/', views.CategoryListView.as_view(), name='cat_list'),

    # CRUD
    path("add/", views.CreateBookView.as_view(), name='add'),
    path("update/<pk>", views.UpdateBookView.as_view(), name='update'),
    path("delete/<pk>", views.DeleteBookView.as_view(), name='delete')
]
