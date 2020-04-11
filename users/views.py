from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model

from .forms import CustomUserChangeForm



class Index(TemplateView):
    template_name = 'index.html'


class CustomUserDetailView(DetailView):
    model = get_user_model()
    template_name = 'users/user_detail.html'


class CustomUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = get_user_model()
    fields = ('avatar', 'first_name', 'last_name', 'city')
    template_name = 'users/user_update.html'

    def test_func(self):
        return self.get_object() == self.request.user
    

