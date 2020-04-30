from datetime import datetime, timedelta

from django.shortcuts import render, HttpResponse, Http404
from django.views.generic import FormView, ListView, UpdateView
from django.http import HttpResponseBadRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .forms import SentenceForSuggestionerForm, ProposalConfirmationForm, BidRejectionForm
from .models import Sentence
from .utils import offer_email, response_to_offer_email



class SentenceForSuggestionerView(LoginRequiredMixin, FormView):
    form_class = SentenceForSuggestionerForm

    def form_invalid(self, form):
        errors_dict = json.dumps(dict([(k, [e for e in v]) for k, v in form.errors.items()]))
        return HttpResponseBadRequest(json.dumps(errors_dict))

    def form_valid(self, form):
        obj = form.save()
        offer_email(obj)
        return HttpResponse('ok')

    def get(self, request, *args, **kwargs):
        return Http404()


class OffersListView(LoginRequiredMixin, ListView):
    model = Sentence
    context_object_name = 'offers'
    template_name = 'sentence/offers_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(whomever_is_offered=self.request.user)
        return queryset
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        time = datetime.today() - timedelta(days=15)
        context['confirmed_offers'] = context['offers'].filter(permission=True, updated_at__gte=time)
        context['offers'] = context['offers'].filter(permission=None)
        return context
        


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
        obj = form.save()
        response_to_offer_email(obj)
        return HttpResponse('ok')


class RejectionOfOfferView(LoginRequiredMixin, UpdateView):
    model = Sentence
    form_class = BidRejectionForm
    template_name = 'sentence/rejection_of_offer.html'
    initial = {
        'permission': False,
    }

    def form_valid(self, form):
        obj = form.save()
        response_to_offer_email(obj)
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
        context['confirmed_offers'] = context['my_offers'].filter(permission=True)[:20]
        context['rejected_offers'] = context['my_offers'].filter(permission=False)[:20]

        return context

class OfferHistoryView(LoginRequiredMixin, ListView):
    model = Sentence
    context_object_name = 'offers'
    template_name = 'sentence/offer_history.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = Q(who_offers=self.request.user) | Q(whomever_is_offered=self.request.user)
        return queryset.filter(q)

