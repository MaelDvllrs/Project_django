from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView

from spotifi.models import Album


class DeleteAlbumView(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = Album
    success_url = '/album/?q='