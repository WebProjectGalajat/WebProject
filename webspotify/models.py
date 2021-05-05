from django.db import models

# Create your models here.

class Sp_User(models.Model):
	spotify_username = models.CharField(max_length=50, default="none")
	django_username = models.CharField(max_length=50, default="user")

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class Favourite_Artist(models.Model):
	spotify_username = models.ForeignKey(Sp_User, max_length=50, default="none", on_delete=models.CASCADE)
	artist_id = models.CharField(max_length=22)
	term = models.CharField(max_length=50)
	position = models.CharField(max_length=50)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class Favourite_Genre(models.Model):
	spotify_username = models.ForeignKey(Sp_User, max_length=50, default="none", on_delete=models.CASCADE)
	genre_name = models.CharField(max_length=50)
	term = models.CharField(max_length=50)
	position = models.CharField(max_length=50)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class Favourite_Song(models.Model):
	spotify_username = models.ForeignKey(Sp_User, max_length=50, default="none", on_delete=models.CASCADE)
	song_id = models.CharField(max_length=22)
	term = models.CharField(max_length=50)
	position = models.CharField(max_length=50)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
