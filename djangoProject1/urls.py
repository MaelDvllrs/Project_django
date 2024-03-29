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
from spotifi.view.Album.createAlbum import AddAlbumView
from spotifi.view.Album.deleteAlbum import DeleteAlbumView
from spotifi.view.Album.deleteMusic import DeleteMusicView
from spotifi.view.Album.updateAlbum import UpdateAlbumView
from spotifi.view.Music import add_music_playlist, remove_music_playlist
from spotifi.view.Style.style_detail import StyleDetail
from spotifi.view.Style.style_list import styleListView
from spotifi.view.addMusic import AddMusicView
from spotifi.view.Album.album_list import albumListView
from spotifi.view.home import HomeView
from spotifi.view.playlist.createPlaylist import CreatePlaylistView
from spotifi.view.playlist.deletePlaylist import DeletePlaylistView
from spotifi.view.playlist.playlist_detail import PlaylistDetail
from spotifi.view.playlist.playlist_list import playlistListView
from spotifi.view.playlist.updatePlaylist import UpdatePlaylistView
from spotifi.view.search import MusicSearchListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('addMusic/',AddMusicView.as_view(), name='addMusic'),
    path('accounts/', include('allauth.urls')),


    path('playlist/', playlistListView.as_view(), name='playlist_list'),
    path('playlist/<int:pk>', PlaylistDetail.as_view(), name='playlist'),
    path('createPlaylist/', CreatePlaylistView.as_view(), name='createPlaylist'),
    path('updatePlaylist/<int:id_playlist>/<int:id_submitter>', UpdatePlaylistView.as_view(), name='updatePlaylist'),
    path('deletePlaylist/<int:pk>', DeletePlaylistView.as_view(), name='deletePlaylist'),
    path('removemusicPlaylist/<int:id_music>/<int:id_playlist>/', remove_music_playlist, name='removemusicPlaylist'),


    path('addmusicPlaylist/<int:id_music>/<int:id_playlist>/<int:id_album>/', add_music_playlist, name='addmusicPlaylist'),
    path('album/', albumListView.as_view(), name='album_list'),
    path('addAlbum/', AddAlbumView.as_view(), name='addAlbum'),
    path('updateAlbum/<int:id_album>/<int:id_submitter>', UpdateAlbumView.as_view(), name='updateAlbum'),
    path('album/<int:pk>', AlbumDetail.as_view(), name='album'),
    path('deleteMusic/<int:pk>', DeleteMusicView.as_view(), name='deleteMusic'),
    path('deleteAlbum/<int:pk>', DeleteAlbumView.as_view(), name='deleteAlbum'),

    path('search/', MusicSearchListView.as_view(), name='music_search'),


    path('style/', styleListView.as_view(), name='style_list'),
    path('style/<int:pk>', StyleDetail.as_view(), name='style'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
