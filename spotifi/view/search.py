from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView
import operator
from functools import reduce

from spotifi.models import Music


class MusicSearchListView(LoginRequiredMixin, ListView):
    model = Music
    template_name = "search.html"


    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Music.objects.filter(
            Q(title__icontains=query)

        )
        return object_list