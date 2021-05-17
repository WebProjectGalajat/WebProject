from django.urls import path
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from webspotify.models import Favourite_Artist
from .forms import ArtistEditForm
from . import views

urlpatterns = [
	path('', views.artist_list, name="artists_list"),
	path('add/', views.CreateArtist.as_view(), name="add_artist"),
	path('<int:pk>/',
	     DetailView.as_view(model=Favourite_Artist,
	                        template_name='webspotify/artists/artist_detail.html'),
	     name="artist_detail"),
	path('<int:pk>/modify/',
	     UpdateView.as_view(model=Favourite_Artist,
	                        template_name='webspotify/artists/artist_modify.html',
	                        form_class=ArtistEditForm),
	     name="modify_artist"),
	path('database_search/', views.database_search, name="database_search_artist")
]
