from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#req -> HttpRequest
def main_url(req):
	return HttpResponse("<h1>Galajat</h1>")

#req -> HttpRequest
def shop_url(req):
	return HttpResponse("<h1>Shop Galajat</h1><h2>Hmmm</h2>")