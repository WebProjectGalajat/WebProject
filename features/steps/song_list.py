from behave import *


@when(u'I list songs')
def step_impl(context):
    # Go to song list page
    context.browser.get(context.get_url('/songs'))


@then(u'I\'m viewing a list containing my songs')
def step_impl(context):
    # Check if we are in the correct page
    assert context.browser.current_url.rstrip("/").split("/")[-1] == "songs"
    # Find the title of the page
    div = context.browser.find_element_by_id('content')
    title = div.find_element_by_tag_name('h1')
    # Check if it has our name
    assert context.user in title.text
