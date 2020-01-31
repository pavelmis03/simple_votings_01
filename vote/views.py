import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from vote.forms import NewVoteForm


def get_base_context():
    context = {
        'menu': [
            {'link': '/', 'text': 'Главная'},
            {'link': '/test', 'text': 'Несуществующая'},
        ],
        'current_time': datetime.datetime.now(),
    }
    return context


def index_page(request):
    context = get_base_context()
    context['title'] = 'Главная страница - simple votings'
    context['main_header'] = 'Simple votings'
    return render(request, 'index.html', context)

def newvote(request):
    context = get_base_context()
    context['title'] = 'Создание нового голосование'
    context['main_header'] = 'Новое голосование'
    if request.method == 'POST':
        f = NewVoteForm(request.POST)
        if f.is_valid():
            return redirect('http://127.0.0.1:8000/')
    form = NewVoteForm()
    context['form'] = form
    return render(request, 'newvote.html', context)
