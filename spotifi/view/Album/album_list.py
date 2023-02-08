from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from spotifi.models.album import Album


class albumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'album_list.html'
