"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.urls import path

from spotifi.view.Album.album_detail import AlbumDetail
from spotifi.view.Music import music_like, add_music_playlist
from spotifi.view.addMusic import AddMusicView
from spotifi.view.Album.album_list import albumListView
from spotifi.view.home import homeView
from spotifi.view.playlist.createPlaylist import CreatePlaylistView
from spotifi.view.playlist.playlist_detail import PlaylistDetail
from spotifi.view.playlist.playlist_list import playlistListView
from spotifi.view.search import MusicSearchListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView.as_view(), name='home'),
    path('addMusic/',AddMusicView.as_view(), name='addMusic'),
    path('accounts/', include('allauth.urls')),
    path('playlist/', playlistListView.as_view(), name=('playlist_list')),
    path('playlist/<int:pk>', PlaylistDetail.as_view(), name='playlist'),
    path('createPlaylist/', CreatePlaylistView.as_view(), name='createPlaylist'),
    path('addmusicPlaylist/<int:id_music>/<int:id_playlist>/<int:id_album>/', add_music_playlist, name='addmusicPlaylist'),
    path('album/', albumListView.as_view(), name=('album_list')),
    path('album/<int:pk>', AlbumDetail.as_view(), name='album'),
    path('like/', music_like, name="music_like"),
    path('search/', MusicSearchListView.as_view(), name='music_search'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
