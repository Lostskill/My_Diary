from urllib import request
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms 
from .models import *
from django.contrib.auth.models import User


class LoginUser(AuthenticationForm):
    username = forms.CharField(label='Логин',widget=forms.TextInput())
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput())



class CreatePage( forms.ModelForm):

    class Meta:
        model = Page_Dairy
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput,
            'text' : forms.Textarea, 
        }