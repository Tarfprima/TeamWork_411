from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . forms import RegistrationForm, LoginForm, ArticleForm
from django.contrib import auth
from . import models

def main(request):
    return render(
        request,
        'article/base.html'
    )

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(
                request,
                'article/register-complete.html',
                {
                    'user': user
                }
            )
    else:
        form = RegistrationForm()
    return render(
        request,
        'article/register.html',
        {
            'form':form
        }
    )

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = auth.authenticate(
                username = cd['username'],
                password = cd['password']
            )
        if user is not None:
            if user.is_active:
                auth.login(request, user)
            return redirect('/')
        else:
            return redirect ('login')
    else:
        form = LoginForm()
    return render(
        request,
        'article/login.html',
        {
            'form': form
        }
    )

def post_list(request):
    object_list = models.Article.objects.all()
    return render(
        request,
        'article/post_list.html',
        {
            'object_list': object_list
        }
    )

def post_form(request):
    form = ArticleForm(request.POST)

    if form.is_valid():
        form.save()

    return render(
        request,
        'article/post_form.html',
        {
            'form':form
        }
    )
