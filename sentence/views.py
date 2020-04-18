import json

from django.shortcuts import render, HttpResponse, Http404
from django.views.generic import FormView, ListView, UpdateView
from django.http import HttpResponseBadRequest

from .forms import SentenceForSuggestionerForm, ProposalConfirmationForm
from .models import Sentence



class SentenceForSuggestionerView(FormView):
    form_class = SentenceForSuggestionerForm

    def form_invalid(self, form):
        errors_dict = json.dumps(dict([(k, [e for e in v]) for k, v in form.errors.items()]))
        return HttpResponseBadRequest(json.dumps(errors_dict))

    def form_valid(self, form):
        form.save()
        return HttpResponse('ok')

    def get(self, request, *args, **kwargs):
        return Http404()


class OffersListView(ListView):
    model = Sentence
    context_object_name = 'offers'
    template_name = 'sentence/offers_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(whomever_is_offered=self.request.user)
        queryset = queryset.filter(permission=None)
        return queryset


class ProposalConfirmationView(UpdateView):
    model = Sentence
    form_class = ProposalConfirmationForm
    template_name = 'sentence/proposal_confirmation_form.html'
    initial = {
        'permission': True,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['books_of_interest_2'].queryset = context['object'].who_offers.my_books.all()
        return context

    def form_valid(self, form):
        form.save()
        return HttpResponse('ok')


