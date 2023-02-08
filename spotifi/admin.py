from django.contrib import admin

from spotifi.models import Music
from spotifi.models.album import Album
from spotifi.models.playlist import Playlist
from spotifi.models.style import Style

# Register your models here.
admin.site.register(Music)
admin.site.register(Album)
admin.site.register(Playlist)
admin.site.register(Style)

