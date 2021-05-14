from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView
# Create your views here.

from .models import *
from .forms import CustomUserCreationForm, SongForm, SongEditForm

scope = 'playlist-modify-private,playlist-modify-public,user-top-read'


# req -> HttpRequest
def main_url(req):
	if req.user.is_authenticated:
		return HttpResponseRedirect("/dashboard/")
	return render(req, 'webspotify/index.html')


# req -> HttpRequest
def dashboard_url(req):
	if not req.user.is_authenticated:
		return HttpResponseRedirect("/")
	return render(req, 'webspotify/dashboard.html')


# req -> HttpRequest
def register_url(req):
	if req.user.is_authenticated:
		return HttpResponseRedirect("/dashboard/")
	if req.method == "GET":
		return render(
			req, "registration/register.html",
			{"form": CustomUserCreationForm}
		)
	elif req.method == "POST":
		form = CustomUserCreationForm(req.POST)
		if form.is_valid():
			user = form.save()
			login(req, user)
			return HttpResponseRedirect("/dashboard/")
		print(form.errors)
		return render(
			req, "registration/register.html",
			{"form": CustomUserCreationForm}
		)

def song_list(req):
	all_songs = Favourite_Song.objects.order_by('user')
	dic = {'songs': []}
	for song in all_songs:
		if song.user == req.user:
			dic['songs'].append(song)
	return render(req, 'webspotify/songs/songs_list.html', dic)


class CreateSong(CreateView):
	model = Favourite_Song
	template_name = "webspotify/songs/add_song.html"
	form_class = SongForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(CreateSong, self).form_valid(form)
