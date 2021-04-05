from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from .models import *


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
