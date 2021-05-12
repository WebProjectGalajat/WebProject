from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def before_all(context):
	opts = Options()
	opts.add_argument('--no-sandbox')
	opts.add_argument('--headless')
	context.browser = Firefox(options=opts)
	pass


def after_all(context):
	context.browser.quit()
	context.browser = None
	pass
