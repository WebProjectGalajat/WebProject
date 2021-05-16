from django.urls import path, include

from . import views
from .songs import views as song_views

urlpatterns = [
	path('', views.main_url, name="index"),
	path('accounts/', include('django.contrib.auth.urls')),
	path('dashboard/', views.dashboard_url, name="dashboard"),
	path('register/', views.register_url, name="register"),
	path('songs/', include('webspotify.songs.urls')),
	path('artists/', include('webspotify.artists.urls')),
	path('genres/', include('webspotify.genres.urls')),
]
