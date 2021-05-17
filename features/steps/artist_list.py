from behave import *


@when(u'I list artists')
def step_impl(context):
    link_to_artists = context.browser.find_elements_by_tag_name('a')


@then(u'the list contains 20 artists')
def step_impl(context):
    raise NotImplementedError("ERROR")
