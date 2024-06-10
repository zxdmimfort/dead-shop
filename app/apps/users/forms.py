from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm

from .models import Client


class UserCreateForm(UserCreationForm):
    email = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = Client
        fields = [
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
        ]

class LoginForm(forms.Form):
    email=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=Client
        fields=["email","password"]
