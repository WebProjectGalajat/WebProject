from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView
from webspotify.models import Favourite_Genre
from .forms import GenreForm


def genre_list(req):
	all_songs = Favourite_Genre.objects.order_by('user')
	dic = {'genres': []}
	for song in all_songs:
		if song.user == req.user:
			dic['genres'].append(song)
	return render(req, 'webspotify/genres/genres_list.html', dic)

def delete_genre(req, pk):
	Favourite_Genre.objects.filter(id=pk).delete()
	return HttpResponseRedirect("/genres/")

def genres_from_file(req):
	if 'term' in req.GET:
		all_genres = [line.rstrip("\n") for line in open("webspotify/genres/genres.txt", "r").readlines()]
		term = req.GET.get('term')
		results = []
		for genre in all_genres:
			if genre.startswith(term) and genre not in results:
				results.append(genre)
				if len(results) >= 10:
					break
		if len(results) < 10:
			for genre in all_genres:
				if term in genre and genre not in results:
					results.append(genre)
					if len(results) >= 10:
						break
		return JsonResponse(results, safe=False)
	return JsonResponse([], safe=False)


class CreateGenre(CreateView):
	model = Favourite_Genre
	template_name = "webspotify/genres/add_genre.html"
	form_class = GenreForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(CreateGenre, self).form_valid(form)
