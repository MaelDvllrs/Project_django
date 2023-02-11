from django.shortcuts import render
from django.views import View


from spotifi.models import Playlist, Music
from spotifi.models.album import Album


class HomeView(View):
    def get(self, request):
        album = Album.objects.all()[:4]
        playlist = Playlist.objects.all()[:4]
        music = Music.objects.all()[:10]
        return render(request, 'home.html', {'album': album, 'playlist': playlist, 'music': music})

    def test_func(self):
        return self.request.user.is_staff