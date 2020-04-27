from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model

from .forms import CustomUserChangeForm

from sentence.forms import SentenceForSuggestionerForm
from sentence.utils import get_contacts_permission



class Index(TemplateView):
    template_name = 'index.html'


class CustomUserDetailView(DetailView):
    model = get_user_model()
    template_name = 'users/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        form = SentenceForSuggestionerForm({
            'who_offers': self.request.user,
            'whomever_is_offered': context['object'],
        })
        form.fields['books_of_interest_1'].queryset = context['object'].my_books.all()
        
        if self.request.user ==  context['object']:
            context['get_contacts_permission'] = True
        else:
            context['get_contacts_permission'] = get_contacts_permission(self.request.user, context['object'])
        context['form'] = form

        return context




class CustomUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = get_user_model()
    fields = ('avatar', 'first_name', 'last_name', 'phone_number', 'city')
    template_name = 'users/user_update.html'

    def test_func(self):
        return self.get_object() == self.request.user
    

