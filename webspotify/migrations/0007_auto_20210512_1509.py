# Generated by Django 3.1.6 on 2021-05-12 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webspotify', '0006_auto_20210512_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite_artist',
            name='spotify_username',
            field=models.ForeignKey(default='usern', max_length=50, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favourite_genre',
            name='spotify_username',
            field=models.ForeignKey(default='usern', max_length=50, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favourite_song',
            name='spotify_username',
            field=models.ForeignKey(default='usern', max_length=50, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Sp_User',
        ),
    ]
