from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


from spotifi.models import Playlist
from spotifi.models.album import Album


class AlbumDetail(LoginRequiredMixin, View):
    def get(self, request, pk):
        album = Album.objects.get(pk=pk)
        playlist = Playlist.objects.filter(submitter=request.user)
        return render(request, 'album.html', {'album': album, 'playlist': playlist})