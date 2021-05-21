from selenium.webdriver.common.keys import Keys
from behave import *

@given(u'Exists a song "{song}" to user "{user}"')
def step_impl(context, song, user):
    from webspotify.models import Favourite_Song
    from django.contrib.auth.models import User
    user_obj = User.objects.filter(username=user)[0]
    Favourite_Song.objects.create(user=user_obj,
                                    name=song,
                                    artist_name="artista",
                                    genre="genre",
                                    rating=3,
                                    description="Descripcio original")

@when(u'I modify song "{song}"')
def stem_impl(context, song):
    # Des de la llista de cançons, entrar a modificar la cançó
    context.browser.get(context.get_url("/songs"))
    div = context.browser.find_element_by_id("content")
    for li in div.find_elements_by_tag_name("li"):
        # Si estem al link correcte, cliquem
        if song in li.text:
            li.find_element_by_tag_name("a").click()
            break
    # Check if the url is correct
    assert context.browser.current_url.rstrip("/").split("/")[-2] == "songs"
    song_id = context.browser.current_url.rstrip("/").split("/")[-1]
    try:
        int(song_id)
    except ValueError:
        raise
    # We are in a correct url
    links = context.browser.find_elements_by_tag_name("a")
    for link in links:
        if "Edit" in link.text:
            link.click()
            break
    assert context.browser.current_url.rstrip("/").split("/")[-3] == "songs"
    song_id = context.browser.current_url.rstrip("/").split("/")[-2]
    try:
        int(song_id)
    except ValueError:
        raise
    # We are in a correct url
    assert context.browser.current_url.rstrip("/").split("/")[-1] == "modify"
    # Escriure una descripcio nova
    form = context.browser.find_element_by_tag_name('form')
    description_box = form.find_element_by_id('id_description')
    description_box.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    description_box.send_keys('Descripcio nova')
    # Submit the form
    context.browser.find_element_by_id('submit_button').click()


@then(u'I\'m viewing the modified song')
def step_impl(context):
    # Check if we got to the details
    assert context.browser.current_url.rstrip("/").split("/")[-2] == "songs"
    song_id = context.browser.current_url.rstrip("/").split("/")[-1]
    try:
        int(song_id)
    except ValueError:
        raise
    div = context.browser.find_element_by_id("content")
    current_desc = div.find_element_by_tag_name("p").text
    assert "original" not in current_desc
