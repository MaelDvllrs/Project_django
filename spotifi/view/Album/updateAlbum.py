from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView

from spotifi import models


class UpdateAlbumView(LoginRequiredMixin, UpdateView):
    template_name = 'update_album.html'
    model = models.Album
    fields = ['title', 'cover']
    success_url = '/album/?q='

    def get_object(self, queryset=None):
        id_submitter = self.kwargs['id_submitter']
        obj = get_object_or_404(models.Album, pk=self.kwargs['id_album'], submitter_id=id_submitter)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_submitter'] = self.kwargs['id_submitter']
        return context