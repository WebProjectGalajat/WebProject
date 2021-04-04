from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=22)
    username = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Favourite_Artist(models.Model):
    user_id = models.CharField(max_length=22)
    artist_id = models.CharField(max_length=22)
    term = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Favourite_Genre(models.Model):
    user_id = models.CharField(max_length=22)
    genre_name = models.CharField(max_length=50)
    term = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Favourite_Song(models.Model):
    user_id = models.CharField(max_length=22)
    song_id = models.CharField(max_length=22)
    term = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
