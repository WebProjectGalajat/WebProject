from behave import *
from selenium.webdriver import ActionChains

use_step_matcher("parse")


@given(u'Exists a user "{user}" with password "{password}"')
def step_impl(context, user, password):
	from django.contrib.auth.models import User
	context.user = user
	context.password = password
	User.objects.create_user(username=user, email='user@example.com', password=password)


@given(u'I login as user "{user}" with password "{password}"')
def step_impl(context, user, password):
	context.browser.get(context.get_url('/accounts/login/'))
	form = context.browser.find_elements_by_tag_name('form')[0]
	user_box = form.find_element_by_id('id_username')
	user_box.send_keys(user)
	password_box = form.find_element_by_id('id_password')
	password_box.send_keys(password)
	login_button = form.find_elements_by_tag_name('input')[-1]
	login_button.click()
	assert context.browser.current_url.rstrip("/").split("/")[-1] == "dashboard"
