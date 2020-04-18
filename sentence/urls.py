from django.urls import path

from .views import SentenceForSuggestionerView, OffersListView, ProposalConfirmationView

app_name = 'sentence'

urlpatterns = [
    path('offering/', SentenceForSuggestionerView.as_view(), name='offering'),
    path('offers_list/', OffersListView.as_view(), name='offer_list'),
    path('proposal_confirmation/<int:pk>/', ProposalConfirmationView.as_view(), name='proposal_confirmation'),
]
