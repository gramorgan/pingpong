from django.views.generic import TemplateView, ListView, CreateView

from pingpong.models import Player


class HomeView(TemplateView):
    template_name = 'home.html'


class PlayersListView(ListView):
    template_name = 'players.html'

    model = Player
    paginate_by = 100


class PlayerCreateView(CreateView):
    template_name = 'create_player.html'

    model = Player
    fields = ['name']
