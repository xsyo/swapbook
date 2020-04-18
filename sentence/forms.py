from django import forms

from book.models import Book

from .models import Sentence


class SentenceForSuggestionerForm(forms.ModelForm):
    
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
