from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView

from spotifi.models import Playlist


class DeletePlaylistView(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = Playlist
    success_url = '/playlist/?q='