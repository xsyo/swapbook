from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'city')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'city')
