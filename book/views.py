from itertools import chain

from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.list import MultipleObjectMixin

from django.contrib.postgres.search import TrigramSimilarity

from .models import Book, BookName, Section, BookAuthor
from .utilities.utils import get_book_and_users, get_users_in_my_city
from .forms import SearchForm
from .utilities.parse_book import get_book


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book/book_list.html'
    ajax_template_name = 'book/book_list_ajax.html'
    paginate_by = 3

    def get_queryset(self):
        try:
            section_id = self.request.GET['section']
            section_id = int(section_id)
            section = Section.objects.get(id=section_id)
        except (KeyError, ValueError, TypeError, Section.DoesNotExist):
            return super().get_queryset()
        else:
            queryset = self.model.objects.filter(section=section)
            return queryset


    def get_template_names(self):
        if self.request.GET:
            return [self.ajax_template_name]
        else:
            return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sections'] = Section.objects.all()
        books = get_book_and_users(self.request.user, context['books'])
        context['books'] = books

        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            context['append_in_list'] = not (context['book'] in self.request.user.my_books.all())
            context['add_to_desired'] = not (context['book'].name in self.request.user.desired_books.all())
        
        context['holders'] = get_users_in_my_city(self.request.user, context['book'])
        
        return context

class BookNameDetailView(DetailView):
    model = BookName
    template_name = 'book/bookName_detail.html'
    context_object_name = 'book_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        books = get_book_and_users(self.request.user, context['book_name'].books.all())
        context['books'] = books

        return context
        



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

    if add_to_desired == 'True':
        user.desired_books.add(book)
    elif add_to_desired == 'False':
        user.desired_books.remove(book)

    return HttpResponse('ok')  


class SearchView(MultipleObjectMixin, FormView):
    form_class = SearchForm
    template_name = 'book/search_book.html'
    ajax_template_name = 'book/book_list_ajax.html'
    context_object_name = 'books'
    paginate_by = 2
    object_list = []

    search_model = {
        'name': BookName,
        'author': BookAuthor,
    }

    def form_valid(self, form):
        query = form.cleaned_data['query']
        search_type = form.cleaned_data['search_type']
        if search_type == 'isbn':
            result = self.search_isbn(query)
        else:
            result = self.search_book_list(query, search_type)
        
        result = get_book_and_users(self.request.user, result)
        
        context = self.get_context_data(object_list=result)
        
        template_name = self.get_template_names()

        return render(self.request, template_name, context)


    def get_template_names(self):
        try:
            if int(self.request.GET['page']) > 1:
                return [self.ajax_template_name]
            else:
                raise KeyError
        except KeyError:
            return super().get_template_names()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['data'] = self.request.GET
        return kwargs
                        
    def get(self, request, *args, **kwargs):
        if request.GET:
            return self.post(request, *args, **kwargs)
        else:
            return super().get(request, *args, **kwargs)

    def search_isbn(self, query):
        try:
            book = get_book(query)
        except Book.DoesNotExist:
            return None
        else:
            return [book]

    def search_book_list(self, query, search_type):
        model = self.search_model[search_type]
        search_result = model.objects.annotate(
                similarity=TrigramSimilarity('name', query),
            ).filter(similarity__gt=0.3).order_by('-similarity')

        if search_type == 'name':
            result = chain(*(bookName.books.all() for bookName in search_result))
        elif search_type == 'author':
            result = chain(*(bookAuthor.author_books.all() for bookAuthor in search_result))
        return result

            

