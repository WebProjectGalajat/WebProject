from django.shortcuts import render
from django.views.generic.edit import CreateView
from webspotify.models import Favourite_Song
from .forms import SongForm
from django.http import HttpResponseRedirect

def song_list(req):
	all_songs = Favourite_Song.objects.order_by('user')
	dic = {'songs': []}
	for song in all_songs:
		if song.user == req.user:
			dic['songs'].append(song)
	return render(req, 'webspotify/songs/songs_list.html', dic)

def delete_song(req, pk):
	Favourite_Song.objects.filter(id=pk).delete()
	return HttpResponseRedirect("/songs/")

class CreateSong(CreateView):
	model = Favourite_Song
	template_name = "webspotify/songs/add_song.html"
	form_class = SongForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(CreateSong, self).form_valid(form)
