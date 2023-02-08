from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from spotifi.models.playlist import Playlist


class PlaylistDetail(LoginRequiredMixin, DetailView):
    template_name = 'playlist.html'
    model = Playlist
