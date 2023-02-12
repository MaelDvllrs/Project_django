from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from spotifi.models import Music


class DeleteMusicView(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = Music
    success_url = reverse_lazy('album_list')


