from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def before_all(context):
	opts = Options()
	opts.headless = True
	opts.add_argument('--no-sandbox')
	# context.browser = Firefox(options=opts)
	pass


def after_all(context):
	# context.browser.quit()
	context.browser = None
	pass
