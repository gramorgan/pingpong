from django.views.generic import TemplateView, ListView, CreateView, DetailView

from pingpong.models import Player


class HomeView(TemplateView):
    template_name = 'home.html'


class PlayersListView(ListView):
    template_name = 'players.html'
    context_object_name = 'players'

    model = Player
    paginate_by = 100


class PlayerDetailView(DetailView):
    template_name = 'player_detail.html'
    context_object_name = 'player'

    model = Player


class PlayerCreateView(CreateView):
    template_name = 'player_create.html'

    model = Player
    fields = ['name']
