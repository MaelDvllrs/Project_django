from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from spotifi.forms.music_form import MusicForm


class AddMusicView(LoginRequiredMixin, CreateView):
    template_name = 'add_music.html'
    form_class = MusicForm
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super(AddMusicView, self).get_form_kwargs()
        kwargs['submitter'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super().form_valid(form)
