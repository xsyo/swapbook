from django.urls import path

from .views import (
                    SentenceForSuggestionerView, OffersListView, 
                    ProposalConfirmationView, RejectionOfOfferView,
                    MySuggestionsView,OfferHistoryView
                    )

app_name = 'sentence'

urlpatterns = [
    path('offer_history/', OfferHistoryView.as_view(), name='offer_history'),
    path('offering/', SentenceForSuggestionerView.as_view(), name='offering'),
    path('offers_list/', OffersListView.as_view(), name='offers_list'),
    path('proposal_confirmation/<int:pk>/', ProposalConfirmationView.as_view(), name='proposal_confirmation'),
    path('rejection_of_offer/<int:pk>/', RejectionOfOfferView.as_view(), name='rejection_of_offer'),
    path('my_suggestions/', MySuggestionsView.as_view(), name='my_suggestions'),
]
