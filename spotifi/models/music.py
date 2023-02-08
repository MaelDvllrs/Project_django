from django.contrib.auth import get_user_model
from django.db import models
from django import forms

from spotifi.models.album import Album
from spotifi.models.style import Style

class Music(models.Model):
    submitter = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.CASCADE, default='')
    album = models.ForeignKey(Album, null=False, blank=False, on_delete=models.CASCADE, default='', related_name='music')
    style = models.ManyToManyField(Style,null=False, blank=False, related_name="music")
    title = models.CharField(max_length=50, blank=False, null=False, default='')
    audio_file = models.FileField(blank=False, null=False, default='')
    like = models.ManyToManyField(get_user_model(), blank=True, related_name="music_like")

    def __str__(self):
        return self.title
