# Generated by Django 4.1.3 on 2023-02-03 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spotifi', '0008_music_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='album',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='music', to='spotifi.album'),
        ),
        migrations.AlterField(
            model_name='music',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='music_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
