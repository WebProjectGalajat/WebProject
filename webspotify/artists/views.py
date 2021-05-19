from django.shortcuts import render
from django.views.generic.edit import CreateView
from webspotify.models import Favourite_Artist
from .forms import ArtistForm
import requests as r
from django.http import JsonResponse, HttpResponseRedirect

def artist_list(req):
	all_songs = Favourite_Artist.objects.order_by('user')
	dic = {'artists': []}
	for song in all_songs:
		if song.user == req.user:
			dic['artists'].append(song)
	return render(req, 'webspotify/artists/artists_list.html', dic)

def delete_artist(req, pk):
	Favourite_Artist.objects.filter(id=pk).delete()
	return HttpResponseRedirect("/artists/")

def database_search(req):
	if 'term' in req.GET:
		response = r.get(
			"https://musicbrainz.org/ws/2/artist?query=" + req.GET.get('term') + "&limit=20&offset=0&fmt=json")
		resp_json = response.json()
		norm_names = [art['name'] for art in resp_json['artists']]
		names = []
		for name in norm_names:
			if name not in names:
				names.append(name)
		while len(names) > 10:
			names = names[:-1]
		return JsonResponse(names, safe=False)
	return JsonResponse([], safe=False)

class CreateArtist(CreateView):
	model = Favourite_Artist
	template_name = "webspotify/artists/add_artist.html"
	form_class = ArtistForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(CreateArtist, self).form_valid(form)
