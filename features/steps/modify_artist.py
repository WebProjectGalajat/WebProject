from selenium.webdriver.common.keys import Keys
from behave import *

@given(u'Exists an artist "{artist}" to user "{user}"')
def step_impl(context, artist, user):
    from webspotify.models import Favourite_Artist
    from django.contrib.auth.models import User
    user_obj = User.objects.filter(username=user)[0]
    Favourite_Artist.objects.create(user=user_obj,
                                    name=artist,
                                    rating=3,
                                    description="Descripcio original")

@when(u'I modify artist "{artist}"')
def step_impl(context, artist):
    # Des de la llista de cançons, entrar a modificar la cançó
    context.browser.get(context.get_url("/artists"))
    div = context.browser.find_element_by_id("content")
    for li in div.find_elements_by_tag_name("li"):
        # Si estem al link correcte, cliquem
        if artist in li.text:
            li.find_element_by_tag_name("a").click()
            break
    # Check if the url is correct
    assert context.browser.current_url.rstrip("/").split("/")[-2] == "artists"
    art_id = context.browser.current_url.rstrip("/").split("/")[-1]
    try:
        int(art_id)
    except ValueError:
        raise
    # We are in a correct url
    links = context.browser.find_elements_by_tag_name("a")
    for link in links:
        if "Edit" in link.text:
            link.click()
            break
    print(context.browser.current_url)
    assert context.browser.current_url.rstrip("/").split("/")[-3] == "artists"
    art_id = context.browser.current_url.rstrip("/").split("/")[-2]
    try:
        int(art_id)
    except ValueError:
        raise
    # We are in a correct url
    assert context.browser.current_url.rstrip("/").split("/")[-1] == "modify"
    # Escriure una descripcio nova
    print(context.browser.current_url)
    form = context.browser.find_element_by_tag_name('form')
    description_box = form.find_element_by_id('id_description')
    description_box.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    description_box.send_keys('Descripcio nova')
    # Submit the form
    context.browser.find_element_by_id('submit_button').click()

@then(u'I\'m viewing the modified artist')
def step_impl(context):
    # Check if we got to the details
    assert context.browser.current_url.rstrip("/").split("/")[-2] == "artists"
    song_id = context.browser.current_url.rstrip("/").split("/")[-1]
    try:
        int(song_id)
    except ValueError:
        raise
    div = context.browser.find_element_by_id("content")
    current_desc = div.find_element_by_tag_name("p").text
    assert "original" not in current_desc
