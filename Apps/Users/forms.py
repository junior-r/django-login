from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    first_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    last_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    email = forms.EmailField(max_length=150, required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
        }
    ))
    password1 = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))
    password2 = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
