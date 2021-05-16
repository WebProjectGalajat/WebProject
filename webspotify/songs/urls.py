from django.urls import path
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from webspotify.models import Favourite_Song
from .forms import SongEditForm
from . import views

urlpatterns = [
	path('', views.song_list, name="songs_list"),
	path('add/', views.CreateSong.as_view(), name="add_song"),
	path('<int:pk>',
	     DetailView.as_view(model=Favourite_Song,
	                        template_name='webspotify/songs/song_detail.html'),
	     name="song_detail"),
	path('<int:pk>/modify/',
	     UpdateView.as_view(model=Favourite_Song,
	                        template_name='webspotify/songs/song_modify.html',
	                        form_class=SongEditForm),
	     name="modify_song")
]