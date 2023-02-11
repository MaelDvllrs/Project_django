from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from spotifi.models.style import Style


class StyleDetail(LoginRequiredMixin, DetailView):
    template_name = 'style.html'
    model = Style