from selenium.webdriver import ActionChains
from behave import *


@when(u'I type a genre "{genre}"')
def step_impl(context, genre):
    context.browser.get(context.get_url('/genres/add/'))
    # Check if we are in correct url
    assert context.browser.current_url.rstrip("/").split("/")[-1] == "add"
    assert context.browser.current_url.rstrip("/").split("/")[-2] == "genres"
    # Find and type song and artist name and description, leave rating as default (3)
    form = context.browser.find_element_by_tag_name('form')
    name_box = form.find_element_by_id('id_name')
    name_box.send_keys(genre)
    context.genre = genre
    description_box = form.find_element_by_id('id_description')
    description_box.send_keys('Descripcio original')
    # Submit the form
    context.browser.find_element_by_id('submit_button').click()

@then(u'I\'m viewing details containing 1 genre')
def step_impl(context):
    assert context.browser.current_url.rstrip("/").split("/")[-2] == "genres"
    genre_id = context.browser.current_url.rstrip("/").split("/")[-1]
    try:
        int(genre_id)
    except ValueError:
        raise
    # We are in a correct url
    div = context.browser.find_element_by_id("content")
    title_tag = context.browser.find_element_by_tag_name("h1")
    assert title_tag.text == context.genre
