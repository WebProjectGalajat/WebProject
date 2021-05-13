from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from WebProjectSpotify.settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
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
def shop_url(req):
	return HttpResponse("<h1>Shop Galajat</h1><h2>Hmmm</h2>")


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
