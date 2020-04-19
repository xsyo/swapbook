import json

from django.shortcuts import render, HttpResponse, Http404
from django.views.generic import FormView, ListView, UpdateView
from django.http import HttpResponseBadRequest
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SentenceForSuggestionerForm, ProposalConfirmationForm, BidRejectionForm
from .models import Sentence



class SentenceForSuggestionerView(LoginRequiredMixin, FormView):
    form_class = SentenceForSuggestionerForm

    def form_invalid(self, form):
        errors_dict = json.dumps(dict([(k, [e for e in v]) for k, v in form.errors.items()]))
        return HttpResponseBadRequest(json.dumps(errors_dict))

    def form_valid(self, form):
        form.save()
        return HttpResponse('ok')

    def get(self, request, *args, **kwargs):
        return Http404()


class OffersListView(LoginRequiredMixin, ListView):
    model = Sentence
    context_object_name = 'offers'
    template_name = 'sentence/offers_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(whomever_is_offered=self.request.user)
        queryset = queryset.filter(permission=None)
        return queryset


class ProposalConfirmationView(LoginRequiredMixin, UpdateView):
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


class RejectionOfOfferView(LoginRequiredMixin, UpdateView):
    model = Sentence
    form_class = BidRejectionForm
    template_name = 'sentence/rejection_of_offer.html'
    initial = {
        'permission': False,
    }

    def form_valid(self, form):
        form.save()
        return HttpResponse('ok')


class MySuggestionsView(LoginRequiredMixin, ListView):
    model = Sentence
    template_name = 'sentence/my_suggestions.html'
    context_object_name = 'my_offers'
    ordering = '-id'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(who_offers=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['unanswered_offers'] = context['my_offers'].filter(permission=None)
        context['confirmed_offers'] = context['my_offers'].filter(permission=True)
        context['rejected_offers'] = context['my_offers'].filter(permission=False)

        return context
