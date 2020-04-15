from django.urls import path

from .views import BookDetailView, add_book_in_user_list, add_book_to_desired

app_name = 'book'

urlpatterns = [
    path('<slug:slug>/', BookDetailView.as_view(), name='book_detail'),
    path('my_books/add/', add_book_in_user_list, name='add_book_in_user_list'),
    path('desired_books/add/', add_book_to_desired, name='add_book_to_desired'),
]
