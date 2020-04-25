from django import forms

class SearchForm(forms.Form):
    CHOICES = (
        ('name', 'Имя книги'),
        ('author', 'Автор'),
        ('isbn', 'ISBN'),
    )

    query = forms.CharField(label='Поиск', required=False)
    search_type = forms.ChoiceField(choices=CHOICES, required=False)

