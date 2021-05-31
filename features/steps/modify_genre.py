from selenium.webdriver.common.keys import Keys
from behave import *

@given(u'Exists a genre "{genre}" to user "{user}"')
def step_impl(context, genre, user):
    from webspotify.models import Favourite_Genre
    from django.contrib.auth.models import User
    user_obj = User.objects.filter(username=user)[0]
    Favourite_Genre.objects.create(user=user_obj,
                                    name=genre,
                                    rating=3,
                                    description="Descripcio original")

@when(u'I modify genre "{genre}"')
def step_impl(context, genre):
    # Des de la llista de cançons, entrar a modificar la cançó
    context.browser.get(context.get_url("/genres"))
    div = context.browser.find_element_by_id("content")
    for li in div.find_elements_by_tag_name("li"):
        # Si estem al link correcte, cliquem
        if genre in li.text:
            li.find_element_by_tag_name("a").click()
            break
    # Check if the url is correct
    assert context.browser.current_url.rstrip("/").split("/")[-2] == "genres"
    genre_id = context.browser.current_url.rstrip("/").split("/")[-1]
    try:
        int(genre_id)
    except ValueError:
        raise
    # We are in a correct url
    links = context.browser.find_elements_by_tag_name("a")
    for link in links:
        if "Edit" in link.text:
            link.click()
            break
    assert context.browser.current_url.rstrip("/").split("/")[-3] == "genres"
    genre_id = context.browser.current_url.rstrip("/").split("/")[-2]
    try:
        int(genre_id)
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

@then(u'I\'m viewing the modified genre')
def step_impl(context):
    # Check if we got to the details
    assert context.browser.current_url.rstrip("/").split("/")[-2] == "genres"
    song_id = context.browser.current_url.rstrip("/").split("/")[-1]
    try:
        int(song_id)
    except ValueError:
        raise
    div = context.browser.find_element_by_id("content")
    current_desc = div.find_element_by_tag_name("p").text
    assert "original" not in current_desc
