from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Favourite_Artist(models.Model):
	spotify_username = models.ForeignKey(User, max_length=50, default="usern", on_delete=models.CASCADE)
	artist_id = models.CharField(max_length=22)
	term = models.CharField(max_length=50)
	position = models.CharField(max_length=50)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class Favourite_Genre(models.Model):
	spotify_username = models.ForeignKey(User, max_length=50, default="usern", on_delete=models.CASCADE)
	genre_name = models.CharField(max_length=50)
	term = models.CharField(max_length=50)
	position = models.CharField(max_length=50)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class Favourite_Song(models.Model):
	spotify_username = models.ForeignKey(User, max_length=50, default="usern", on_delete=models.CASCADE)
	song_id = models.CharField(max_length=22)
	term = models.CharField(max_length=50)
	position = models.CharField(max_length=50)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
