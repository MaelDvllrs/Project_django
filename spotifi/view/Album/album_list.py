from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView

from spotifi.models.album import Album


class albumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'album_list.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Album.objects.filter(
            Q(title__icontains=query)
        )
        return object_list
