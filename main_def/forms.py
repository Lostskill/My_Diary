from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms 

class LoginUser(AuthenticationForm):
    username = forms.CharField(label='Логин',widget=forms.TextInput())
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput())