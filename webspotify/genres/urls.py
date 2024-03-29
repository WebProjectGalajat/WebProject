from django.urls import path
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from webspotify.models import Favourite_Genre
from .forms import GenreEditForm
from . import views

urlpatterns = [
	path('', views.genre_list, name="genres_list"),
	path('add/', views.CreateGenre.as_view(), name="add_genre"),
	path('<int:pk>/',
	     DetailView.as_view(model=Favourite_Genre,
	                        template_name='webspotify/genres/genre_detail.html'),
	     name="genre_detail"),
	path('<int:pk>/modify/',
	     UpdateView.as_view(model=Favourite_Genre,
	                        template_name='webspotify/genres/genre_modify.html',
	                        form_class=GenreEditForm),
	     name="modify_genre"),
	path('database_search/', views.genres_from_file, name="genres_from_file"),
	path('<int:pk>/delete/', views.delete_genre, name="delete_genre")
]
