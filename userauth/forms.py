from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class register_form(UserCreationForm):
    email = forms.EmailField(required=True, help_text=None)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
