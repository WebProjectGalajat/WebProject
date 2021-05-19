from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login
# Create your views here.

from .forms import CustomUserCreationForm


# req -> HttpRequest
def main_url(req):
	if req.user.is_authenticated:
		return HttpResponseRedirect("/dashboard/")
	return render(req, 'webspotify/index.html')


# req -> HttpRequest
def dashboard_url(req):
	if not req.user.is_authenticated:
		return HttpResponseRedirect("/")
	return render(req, 'webspotify/dashboard.html')


# req -> HttpRequest
def register_url(req):
	if req.user.is_authenticated:
		return HttpResponseRedirect("/dashboard/")
	if req.method == "GET":
		return render(
			req, "registration/register.html",
			{"form": CustomUserCreationForm}
		)
	elif req.method == "POST":
		form = CustomUserCreationForm(req.POST)
		if form.is_valid():
			user = form.save()
			login(req, user)
			return HttpResponseRedirect("/dashboard/")
		print(form.errors)
		return render(
			req, "registration/register.html",
			{"form": CustomUserCreationForm}
		)
