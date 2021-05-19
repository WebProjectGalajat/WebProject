from selenium.webdriver import ActionChains
from behave import *


@when(u'I modify artist "{artist_name}"')
def step_impl(context, artist_name):
    from webspotify.models import Favourite_Artist
    artist = Favourite_Artist.objects.get(name=artist_name)
