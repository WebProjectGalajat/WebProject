from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import *


# req -> HttpRequest
def main_url(req):
	return render(req, 'webspotify/index.html')


# req -> HttpRequest
def shop_url(req):
	return HttpResponse("<h1>Shop Galajat</h1><h2>Hmmm</h2>")
