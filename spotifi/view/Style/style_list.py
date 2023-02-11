from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView

from spotifi.models.style import Style


class styleListView(LoginRequiredMixin, ListView):
    model = Style
    template_name = 'style_list.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Style.objects.filter(
            Q(name__icontains=query)
        )
        return object_list