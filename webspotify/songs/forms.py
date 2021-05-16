from django.forms import ModelForm
from webspotify.models import Favourite_Song


class SongForm(ModelForm):
	class Meta:
		model = Favourite_Song
		exclude = ('user',)


class SongEditForm(ModelForm):
	class Meta:
		model = Favourite_Song
		exclude = ('user', 'name', 'artist_name')
