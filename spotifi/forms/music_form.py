from django import forms

from spotifi import models
from spotifi.models.album import Album


class MusicForm(forms.ModelForm):
    class Meta:
        model = models.Music
        fields = ['title', 'album', 'style', 'audio_file']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('submitter')
        super(MusicForm, self).__init__(*args, **kwargs)
        self.fields['album'].queryset = models.album.Album.objects.filter(submitter=user)
