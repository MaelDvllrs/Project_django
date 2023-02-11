from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from spotifi.forms.album_form import AlbumForm


class AddAlbumView(LoginRequiredMixin, CreateView):
    template_name = 'add_album_.html'
    form_class = AlbumForm
    success_url = reverse_lazy('album_list')

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super().form_valid(form)