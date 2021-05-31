from django.shortcuts import render
from django.views.generic.edit import CreateView
from webspotify.models import Favourite_Artist
from .forms import ArtistForm
import requests as r
from django.http import JsonResponse, HttpResponseRedirect


def artist_list(req):
	if not req.user.is_authenticated:
		return HttpResponseRedirect("/")
	all_songs = Favourite_Artist.objects.order_by('user')
	dic = {'artists': []}
	for song in all_songs:
		if song.user == req.user:
			dic['artists'].append(song)
	return render(req, 'webspotify/artists/artists_list.html', dic)


def delete_artist(req, pk):
	if not req.user.is_authenticated:
		return HttpResponseRedirect("/")
	Favourite_Artist.objects.filter(id=pk).delete()
	return HttpResponseRedirect("/artists/")


def database_search(req, as_list=False, term=None):
	if not as_list:
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
	else:
		if term is not None:
			response = r.get(
				"https://musicbrainz.org/ws/2/artist?query=" + term.replace(" ", "+") + "&limit=20&offset=0&fmt=json")
			resp_json = response.json()
			norm_names = [art['name'] for art in resp_json['artists']]
			names = []
			for name in norm_names:
				if name not in names:
					names.append(name)
			while len(names) > 10:
				names = names[:-1]
			return names
		return []


def get_my_artists(req):
	response = []
	if 'term' in req.GET:
		my_artists = Favourite_Artist.objects.all()
		for art in my_artists:
			if art.name.startswith(req.GET.get('term')):
				response.append(art.name)
			if len(response) >= 10:
				break
	print(response)
	if len(response) < 10:
		response += database_search(None, as_list=True, term=req.GET.get('term'))
	print(response)
	while len(response) > 10:
		response = response[:-1]
	print(response)
	return JsonResponse(response, safe=False)


class CreateArtist(CreateView):
	model = Favourite_Artist
	template_name = "webspotify/artists/add_artist.html"
	form_class = ArtistForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(CreateArtist, self).form_valid(form)
