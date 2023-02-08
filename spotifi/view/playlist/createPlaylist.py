from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from spotifi.forms.playlist_form import PlaylistForm


class CreatePlaylistView(LoginRequiredMixin, CreateView):
    template_name = 'add_playlist.html'
    form_class = PlaylistForm
    success_url = reverse_lazy('playlist_list')

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super().form_valid(form)
