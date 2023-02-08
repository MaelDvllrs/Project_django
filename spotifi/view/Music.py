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

register = template.Library()


def music_like(request):
    print("test")
    music = get_object_or_404(Music, title=get('music_like'))
    print("music :" + str(music))
    music.like.add(request.get_user_model())
    return HttpResponseRedirect('home')


def add_music_playlist(request, id_music, id_playlist, id_album):

    music_add = Music.objects.get(pk=id_music)
    playlist = Playlist.objects.get(pk=id_playlist)
    album = Album.objects.get(pk=id_album)
    playlist.music.add(music_add)
    url = '/album/' + str(album.id)
    return redirect(url)





# @register.inclusion_tag('base.html')
# def music(request):
#   paginator = Paginator(Music.objects.all(), 1)
#    page_number = request.GET.get('page')
#    page_obj = paginator.get_page(page_number)
#    context = {"page_obj": page_obj}
#    return render(request, "base.html", context)
