from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
	path('', views.main_url),
	path('accounts/', include("django.contrib.auth.urls")),
	path('shop/', views.shop_url)
]