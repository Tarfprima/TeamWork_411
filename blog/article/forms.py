from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']
    
    class Meta:
        model = User
        fields = {
            'username',
            'first_name'
        }

        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
        }

        help_texts = {
            'username': '',
        }

class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

from . import models

class ArticleForm(forms.ModelForm):

    class Meta:
        model = models.Article

        fields = [
            'title',
            'text'
        ]

        labels = {
            'title': 'Заголовок',
            'text': 'Текст',
        }

        
