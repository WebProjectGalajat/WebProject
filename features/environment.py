from splinter.browser import Browser
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def before_all(context):
	options = Options()
	# chrome_options.add_argument('--disable-dev-shm-usage')
	# chrome_options.add_argument('--no-sandbox')
	options.headless = True
	context.browser = webdriver.Firefox(options=options)
	pass


def after_all(context):
	context.browser.quit()
	context.browser = None
	pass
