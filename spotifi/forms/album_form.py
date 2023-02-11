from django import forms


from spotifi import models


class AlbumForm(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = ['title', 'cover']