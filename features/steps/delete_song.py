from selenium.webdriver.common.keys import Keys
from behave import *


@when(u'I delete a song "{song}"')
def step_impl(context, song):
    # From the song list, enter to delete the song
    context.browser.get(context.get_url("/songs"))
    div = context.browser.find_element_by_id("content")
    for li in div.find_elements_by_tag_name("li"):
        # If we are in the correct link, click
        if song in li.text:
            li.find_element_by_tag_name("a").click()
            break
    # Check if the URL is correct
    assert context.browser.current_url.rstrip("/").split("/")[-2] == "songs"
    song_id = context.browser.current_url.rstrip("/").split("/")[-1]
    try:
        int(song_id)
    except ValueError:
        raise
    # We are in the correct URL
    links = context.browser.find_elements_by_tag_name("a")
    for link in links:
        if "Delete" in link.text:
            link.click()
            break
    assert context.browser.current_url.rstrip("/").split("/")[-1] == "songs"


@then(u'I\'m viewing a list without song "{song}"')
def step_impl(context, song):
    assert context.browser.current_url.rstrip("/").split("/")[-1] == "songs"
    div = context.browser.find_element_by_id('content')
    for li in div.find_elements_by_tag_name("li"):
        if song in li.text:
            raise
