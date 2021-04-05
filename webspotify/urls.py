from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
	path('', views.main_url, name="index"),
	path('accounts/', include("django.contrib.auth.urls")),
	path('shop/', views.shop_url),
	path('dashboard/', views.dashboard_url, name="dashboard")
]
