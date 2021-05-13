from django.contrib import admin
from django.urls import path, include
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from webspotify.models import Favourite_Song
from webspotify.forms import SongForm, SongEditForm

from . import views

urlpatterns = [
	path('', views.main_url, name="index"),
	path('accounts/', include("django.contrib.auth.urls")),
	path('shop/', views.shop_url),
	path('dashboard/', views.dashboard_url, name="dashboard"),
	path('register/', views.register_url, name="register"),
	path('songs/add/',
	     CreateView.as_view(model=Favourite_Song,
	                        template_name='webspotify/add_song.html',
	                        form_class=SongForm),
	     name="add_song"),
	path('songs/<int:pk>',
	     DetailView.as_view(model=Favourite_Song,
	                        template_name='webspotify/song_detail.html'),
	     name="song_detail"),
	path('songs/<int:pk>/modify/',
	     UpdateView.as_view(model=Favourite_Song,
	                        template_name='webspotify/song_modify.html',
	                        form_class=SongEditForm),
	     name="modify_song"),
]
