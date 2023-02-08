from django import forms

from spotifi import models


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = models.Playlist
        fields = ['name', 'image_playlist', 'music', 'public']

