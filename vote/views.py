from datetime import datetime

from django.contrib import messages, auth
from django.contrib.auth import *
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from vote.forms import LoginForm


def get_base_context(request, pagename=''):
    context = {'MenuMain': [
        {'punct_link': '/', 'punct_text': 'Nahui'},
    ], 'current_time': datetime.now(), 'MenuMainAnon': [],
        'pagename': pagename}
    if request.user.is_anonymous:
        context['MenuMainAnon'].append({'punct_link': '/login', 'punct_text': 'LogIn'})
        context['MenuMainAnon'].append({'punct_link': '/registration', 'punct_text': 'Register'})
    else:
        context['MenuMainAnon'].append({'punct_link': '/logout', 'punct_text': 'LogOut'})
    return context


def index_page(request):
    context = get_base_context(request, 'Simple votings')
    context['main_header'] = context['title'] = 'Simple votings'
    return render(request, 'pages/index.html', context)


def login_page(request):
    context = get_base_context(request, '')
    context['form'] = LoginForm()
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = loginform.data['username']
            password = loginform.data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Authentication is successful!")
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, "Incorrect username or password!")
        else:
            messages.add_message(request, messages.ERROR, "Incorrect authorization data!")
        return redirect('login')
    return render(request, 'pages/login_page.html', context)


def registration_page(request):
    context = get_base_context(request, '')
    context['form'] = UserCreationForm()
    if request.POST:
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            # Get data
            _username = register_form.cleaned_data['username']
            _password = register_form.cleaned_data['password2']

            # Result
            newuser = authenticate(username=_username, password=_password)
            login(request, newuser)
            return redirect('/')
        else:
            context['form'] = register_form
            for mess in register_form.error_messages:
                messages.add_message(request, messages.ERROR, mess)
            if not register_form.error_messages:
                messages.add_message(request, messages.ERROR, 'Incorrect registration data!')
            return redirect('registration')

    return render(request, 'pages/registration_page.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')