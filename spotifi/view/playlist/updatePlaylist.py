from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from spotifi import models


class UpdatePlaylistView(LoginRequiredMixin, UpdateView):
    template_name = 'update_playlist.html'
    model = models.Playlist
    fields = ['name', 'image_playlist', 'public']
    success_url = '/playlist/?q='
    def get_object(self, queryset=None):
        id_submitter = self.kwargs['id_submitter']
        obj = get_object_or_404(models.Playlist, pk=self.kwargs['id_playlist'], submitter_id=id_submitter)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_submitter'] = self.kwargs['id_submitter']
        return context