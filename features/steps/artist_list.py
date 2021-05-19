from behave import *


@when(u'I list artists')
def step_impl(context):
    context.browser.get(context.get_url("/artists"))


@then(u'I\'m viewing a list containing 20 artists')
def step_impl(context):
    divs = context.browser.find_elements_by_tag_name('div')
    for div in divs:
        if div.id == "content":
            tags = div.find_elements_by_tag_name('li')
            assert len(tags) >= 1
