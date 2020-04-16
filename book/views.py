from django.shortcuts import render, HttpResponse
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from .models import Book, BookName

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            context['append_in_list'] = not (context['book'] in self.request.user.my_books.all())
            context['add_to_desired'] = not (context['book'].name in self.request.user.desired_books.all())
        
        return context

class BookNameDetailView(DetailView):
    model = BookName
    template_name = 'book/bookName_detail.html'
    context_object_name = 'book_name'


@login_required
@require_POST
def add_book_in_user_list(request):
    try:
        book = Book.objects.get(id=request.POST['book_id'])
    except Book.DoesNotExist:
        return HttpResponseBadRequest("Книга не найдена.")

    append_in_list = request.POST['append_in_list']
    user = request.user

    if append_in_list == 'true':
        user.my_books.add(book)
    elif append_in_list == 'false':
        user.my_books.remove(book)

    return HttpResponse('ok')

@login_required
@require_POST
def add_book_to_desired(request):
    try:
        book = BookName.objects.get(id=request.POST['book_name_id'])
    except BookName.DoesNotExist:
        return HttpResponseBadRequest("Книга не найдена.")
    
    add_to_desired = request.POST['add_to_desired']
    user = request.user

    print(book)
    print(type(add_to_desired), add_to_desired)

    if add_to_desired == 'True':
        user.desired_books.add(book)
    elif add_to_desired == 'False':
        user.desired_books.remove(book)

    return HttpResponse('ok')  

