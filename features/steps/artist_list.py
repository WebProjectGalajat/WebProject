from behave import *

@when(u'I list artists')
def step_impl(context):
	context.browser.visit(context.get_url('')) #Falta ficar la URL


@then(u'the list contains 20 artists')
def step_impl(context):
	raise NotImplementedError("ERROR")