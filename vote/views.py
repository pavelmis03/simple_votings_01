from datetime import datetime
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render


def get_base_context(request):
    context = {
        'MenuMain': [
            {'punct_link': '/', 'punct_text': 'Main'},
        ],
        'current_time': datetime.now(),
    }
    context['MenuMainAnon'] = []
    if (request.user.is_anonymous):
        context['MenuMainAnon'].append({'punct_link': '/test', 'punct_text': 'SignIn'})
        context['MenuMainAnon'].append({'punct_link': '/test', 'punct_text': 'Register'})
    return context


def index_page(request):
    context = get_base_context(request)
    context['title'] = 'Главная страница - simple votings'
    context['main_header'] = 'Simple votings'
    return render(request, 'index.html', context)
