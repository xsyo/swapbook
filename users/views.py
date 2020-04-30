from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.core.mail import mail_admins
from django.template.loader import render_to_string
from django.forms import HiddenInput

from .forms import CustomUserChangeForm, FeedbackForm

from sentence.forms import SentenceForSuggestionerForm
from sentence.utils import get_contacts_permission



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
    
class FeedBackFormView(FormView):
    form_class = FeedbackForm
    template_name = 'users/feedback_form.html'

    def get_initial(self):
        if self.request.user.is_authenticated:
            initial = {
                'is_authenticated': True,
                'email': self.request.user.email,
            }
        else:
            initial = {
                'is_authenticated': False,
            }
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        if self.request.user.is_authenticated:
            form.fields['email'].widget = HiddenInput()
        return form

    def form_valid(self, form):
        text = render_to_string('users/email/admin_email.txt', context=form.cleaned_data)
        mail_admins('Связь с администрацией сайта SwapBook', text, fail_silently=True)
        return HttpResponse('ok')
