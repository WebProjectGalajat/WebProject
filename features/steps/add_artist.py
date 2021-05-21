from selenium.webdriver import ActionChains
from behave import *


@when(u'I type an artist "{artist}"')
def step_impl(context, artist):
    context.browser.get(context.get_url('/artists/add/'))
    # Check if we are in correct url
    assert context.browser.current_url.rstrip("/").split("/")[-1] == "add"
    assert context.browser.current_url.rstrip("/").split("/")[-2] == "artists"
    # Find and type artist name and description, leave rating as default (3)
    form = context.browser.find_element_by_tag_name('form')
    name_box = form.find_element_by_id('id_name')
    name_box.send_keys(artist)
    context.artist = artist
    description_box = form.find_element_by_id('id_description')
    description_box.send_keys('Descripcio original')
    # Submit the form
    context.browser.find_element_by_id('submit_button').click()


@then(u'I\'m viewing the artist details containing 1 artist')
def step_impl(context):
    assert context.browser.current_url.rstrip("/").split("/")[-2] == "artists"
    art_id = context.browser.current_url.rstrip("/").split("/")[-1]
    try:
        int(art_id)
    except ValueError:
        raise
    # We are in a correct url
    div = context.browser.find_element_by_id("content")
    title_tag = context.browser.find_element_by_tag_name("h1")
    assert title_tag.text == context.artist
