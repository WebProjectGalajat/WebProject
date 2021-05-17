from behave import *


@when(u'I list songs')
def step_impl(context):
    context.browser.visit(context.get_url(''))  # Falta ficar la URL


@then(u'the list contains 30 songs')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the list contains 30 songs')
