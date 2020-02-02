from datetime import datetime

from django.contrib import messages, auth
from django.contrib.auth import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.utils import timezone

from vote.forms import LoginForm
from vote.models import Post, Answer


def get_base_context(request, pagename=''):
    context = {'MenuMain': [], 'current_time': datetime.now(), 'MenuMainAnon': [], 'pagename': pagename}

    if request.user.is_anonymous:
        context['MenuMainAnon'].append({'punct_link': '/login', 'punct_text': 'Войти'})
        context['MenuMainAnon'].append({'punct_link': '/registration', 'punct_text': 'Зарегистрироваться'})
    else:
        context['MenuMain'] += [{'punct_link': '/add_new_voting', 'punct_text': 'vote'}]
        context['MenuMainAnon'] += [{'punct_link': '/profile', 'punct_text': 'Profile'}]

    return context


def add_new_voting(request):
    context = get_base_context(request, '')
    data = request.POST
    if data:
        post = Post(
            author = request.user,
            type = 'type' in data['text'],
            text = data['text'] if 'text' in data.keys() else '',
            created_at = datetime.now(tz=timezone.utc)
        )
        post.save()
        for i in [_ for _ in data.keys() if 'var' in _]:
            answer = Answer(
                post = post,
                text = data[i]
            )
            answer.save()
    return redirect('/')


def votes(request):
    context = get_base_context(request, '')
    return render(request, 'pages/votes.html', context)


def index_page(request):
    context = get_base_context(request, 'Simple votings')
    context['main_header'] = context['title'] = 'Simple votings'
    context['form'] = LoginForm()
    context['form1'] = UserCreationForm()
    if request.POST:
        register_form = UserCreationForm(request.POST)
        loginform = LoginForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            # Get data
            _username = register_form.cleaned_data['username']
            _password = register_form.cleaned_data['password2']
            # Result
            newuser = authenticate(username=_username, password=_password)
            login(request, newuser)
            messages.add_message(request, messages.SUCCESS, "Вы успешно зарегистрировались и авторизовались!")
            return redirect('/')
        else:
            context['form1'] = register_form
            if loginform.is_valid():
                username = loginform.data['username']
                password = loginform.data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, "Вы успешно вошли!")
                    return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'переданные данные не корректны!')
                return redirect('/')

    posts = Post.objects.all()
    context['posts'] = posts
    answers = Answer.objects.all()
    context['answers'] = answers
    return render(request, 'pages/index.html', context)


def login_page(request):
    pass

def registration_page(request):
    pass


def change_password(request):
    context = get_base_context(request, '')
    context['user'] = request.userпше
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "The password change is successful!")
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, "Incorrectly passwords data!")

    else:
        form = PasswordChangeForm(user=request.user)
        context['form'] = form
    return render(request, 'pages/change_password.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')


def error_404(request, ex):
    context = {'exception': ''}
    try:
        context['exception'] = ex.args[0]
    except (AttributeError, IndexError):
        pass
    return render(request, 'error_pages/error_404.html', context)


def error_500(request):
    return render(request, 'error_pages/error_500.html', {})