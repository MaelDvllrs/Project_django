from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView

from spotifi.models.playlist import Playlist


class playlistListView(LoginRequiredMixin, ListView):
    model = Playlist
    template_name = 'playlist_list.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Playlist.objects.filter(
            Q(name__icontains=query)

        )
        return object_list
