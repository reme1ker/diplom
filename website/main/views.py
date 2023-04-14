from django.shortcuts import render
from django.views.generic import DetailView

from .models import Games


def index(request):
    games = Games.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта',
                                               'games': games})


def about(request):
    return render(request, 'main/about.html')


class GameDetailView(DetailView):
    model = Games
    template_name = 'main/game_detail.html'
