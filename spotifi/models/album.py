from django.contrib.auth import get_user_model
from django.db import models


class Album(models.Model):
    submitter = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.CASCADE, default='')
    title = models.CharField(max_length=50, blank=False, null=True, default='')
    cover = models.ImageField(blank=False, null=True, default='')

    def __str__(self):
        return self.title

