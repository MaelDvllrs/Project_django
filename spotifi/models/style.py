from django.db import models

class Style(models.Model):
   name = models.CharField(max_length=100, null=True, blank=True, default='')
   image_style = models.ImageField(blank=True, null=True, default='')
   def __str__(self):
      return self.name