from django.forms import ModelForm
from webspotify.models import Favourite_Artist


class ArtistForm(ModelForm):
	class Meta:
		model = Favourite_Artist
		exclude = ('user',)


class ArtistEditForm(ModelForm):
	class Meta:
		model = Favourite_Artist
		exclude = ('user', 'name',)
