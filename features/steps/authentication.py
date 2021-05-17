from behave import *

use_step_matcher("parse")


@given(u'Exists a user "{user}" with password "{password}"')
def step_impl(context, user, password):
	from django.contrib.auth.models import User
	context.user = user
	context.password = password
	User.objects.create_user(username=user, email='user@example.com', password=password)


@given(u'I login as user "{user}" with password "{password}"')
def step_impl(context, user, password):
	context.browser.visit(context.get_url('/accounts/login/'))
	form = context.browser.find_elements_by_tag_name('form')[0]
	context.browser.fill('username', user)
	context.browser.fill('password', password)
	form.find_elements_by_value('login')[0].click()
