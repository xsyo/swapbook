from django import forms

from book.models import Book

from .models import Sentence


class SentenceForSuggestionerForm(forms.ModelForm):
    '''Форма для предложения обмена'''
    class Meta:
        model = Sentence
        fields = ('who_offers', 'whomever_is_offered', 'books_of_interest_1', 'message_1')
        widgets = {
            'who_offers': forms.HiddenInput,
            'whomever_is_offered': forms.HiddenInput,
            'books_of_interest_1': forms.CheckboxSelectMultiple,
        }
        labels = {
            'books_of_interest_1': 'Выберите книги которые вас интересуют',
            'message_1': 'Сообщение'
        }

class ProposalConfirmationForm(forms.ModelForm):
    '''Форма для подтверждения обмена'''
    class Meta:
        model = Sentence
        fields = ('books_of_interest_2', 'permission')
        widgets = {
            'books_of_interest_2': forms.CheckboxSelectMultiple,
            'permission': forms.HiddenInput,
        }
        labels = {
            'books_of_interest_2': 'Выберите книги которые вас интересуют',
        }


class BidRejectionForm(forms.ModelForm):
    '''форма отказа обмена'''
    class Meta:
        model = Sentence
        fields = ('reason_for_refusal', 'permission')
        widgets = {
            'permission': forms.HiddenInput,
        }
        labels = {
            'reason_for_refusal': 'Сообщение с причиной отказа',
        }

