from django.contrib.auth import get_user_model
from django.db import models

from spotifi.models import Music


class Playlist(models.Model):
    submitter = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=100, null=True, blank=True, default='')
    image_playlist = models.ImageField(blank=True, null=True, default='')
    music = models.ManyToManyField(Music, null=True, blank=True, related_name="music")
    public = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self):
        return self.name
