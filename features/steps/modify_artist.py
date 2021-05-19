from selenium.webdriver import ActionChains
from behave import *


@when(u'I modify artist "{artist}"')
def step_impl(context, artist):
    from webspotify.models import Favourite_Artist
    artist = Favourite_Artist.objects.get(name=artist_name)

@then(u'I\'m viewing the modified artist "{artist}"')
def step_impl(context, artist):
    raise NotImplementedError(u'STEP: Then I\'m viewing the modified artist "artist"')
