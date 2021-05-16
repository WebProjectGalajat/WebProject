from django.shortcuts import render
from django.views.generic.edit import CreateView
from webspotify.models import Favourite_Artist
from .forms import ArtistForm

def artist_list(req):
	all_songs = Favourite_Artist.objects.order_by('user')
	dic = {'artists': []}
	for song in all_songs:
		if song.user == req.user:
			dic['artists'].append(song)
	return render(req, 'webspotify/artists/artists_list.html', dic)


class CreateArtist(CreateView):
	model = Favourite_Artist
	template_name = "webspotify/artists/add_artist.html"
	form_class = ArtistForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(CreateArtist, self).form_valid(form)
