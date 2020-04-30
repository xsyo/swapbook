from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms



class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'city')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'city')

class FeedbackForm(forms.Form):
    email = forms.EmailField()
    is_authenticated = forms.BooleanField(widget=forms.HiddenInput)
    text = forms.CharField(label='Введите сообщение для администрации', widget=forms.Textarea)
