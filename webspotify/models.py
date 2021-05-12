from django.db import models
from django.contrib.auth.models import User
from django.urls.base import reverse


# Create your models here.


class Favourite_Artist(models.Model):
	user = models.ForeignKey(User, max_length=50, default=1, on_delete=models.CASCADE)
	name = models.CharField(max_length=50, default="")
	RATING_CHOICES = ((0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
	rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
	description = models.TextField(max_length=200, default="")

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class Favourite_Genre(models.Model):
	user = models.ForeignKey(User, max_length=50, default=1, on_delete=models.CASCADE)
	name = models.CharField(max_length=50, default="")
	RATING_CHOICES = ((0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
	rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
	description = models.TextField(max_length=200, default="")

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class Favourite_Song(models.Model):
	user = models.ForeignKey(User, max_length=50, default=1, on_delete=models.CASCADE)
	name = models.CharField(max_length=50, default="")
	artist_name = models.CharField(max_length=50, default="")
	RATING_CHOICES = ((0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
	rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
	description = models.TextField(max_length=200, default="")

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse('song_detail', kwargs={'pk': self.pk})
