from behave import *


@when(u'I list genres')
def step_impl(context):
    context.browser.get(context.get_url("/genres/"))


@then(u'I\'m viewing a list containing my genres')
def step_impl(context):
    # Check if we are in the correct page
    assert context.browser.current_url.rstrip("/").split("/")[-1] == "genres"
    # Find the title of the page
    div = context.browser.find_element_by_id('content')
    title = div.find_element_by_tag_name('h1')
    # Check if it has our name
    assert context.user in title.text
