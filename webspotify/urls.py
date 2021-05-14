from django.contrib import admin
from django.urls import path, include
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth import views as django_views
from webspotify.models import Favourite_Song
from webspotify.forms import SongForm, SongEditForm

from . import views

urlpatterns = [
	path('', views.main_url, name="index"),
	path('accounts/', include('django.contrib.auth.urls')),
	path('dashboard/', views.dashboard_url, name="dashboard"),
	path('register/', views.register_url, name="register"),
	path('songs/', views.song_list, name="songs_list"),
	path('songs/add/', views.CreateSong.as_view(), name="add_song"),
	path('songs/<int:pk>',
	     DetailView.as_view(model=Favourite_Song,
	                        template_name='webspotify/songs/song_detail.html'),
	     name="song_detail"),
	path('songs/<int:pk>/modify/',
	     UpdateView.as_view(model=Favourite_Song,
	                        template_name='webspotify/songs/song_modify.html',
	                        form_class=SongEditForm),
	     name="modify_song"),
]
