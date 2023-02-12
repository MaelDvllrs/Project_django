from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404, redirect, render, resolve_url

# imported our models
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import RedirectView, UpdateView, TemplateView
from requests import get

from spotifi.models import Music, Playlist, Album

def add_music_playlist(request, id_music, id_playlist, id_album):

    music_add = Music.objects.get(pk=id_music)
    playlist = Playlist.objects.get(pk=id_playlist)
    album = Album.objects.get(pk=id_album)
    playlist.music.add(music_add)
    return redirect('album', pk=str(album.id))

def remove_music_playlist(request,  id_music, id_playlist):
    music_add = Music.objects.get(pk=id_music)
    playlist = Playlist.objects.get(pk=id_playlist)
    playlist.music.remove(music_add)
    return redirect('playlist', pk=str(playlist.id))

