from django.forms import ModelForm
from webspotify.models import Favourite_Genre


class GenreForm(ModelForm):
	class Meta:
		model = Favourite_Genre
		exclude = ('user',)


class GenreEditForm(ModelForm):
	class Meta:
		model = Favourite_Genre
		exclude = ('user', 'name', 'artist_name')
