from selenium.webdriver import ActionChains


@when(u'I type a song that is correct')
def step_impl(context, song):
    context.browser.get(context.get_url('songs/'))
    form = context.browser.find_element_by_tag_name('form')
    name_box = form.find_element_by_id('id_name')
    name_box.send_keys(song)
    description_box = form.find_element_by_id('id_description')
    description_box.send_keys('Descripcio original')
    submit_button = form.find_element_by_tag_name('input')[-1]
    ActionChains(context.browser).click(submit_button).perform()


@then(u'I\'m viewing a list containing 1 song')
def step_impl(context):
    context.browser.get(context.get_url('/songs/'))
    divs = context.browser.find_element_by_tag_name('div')
    for div in divs:
        if div.id == "content":
            tags = div.find_element_by_tag_name('li')
            assert len(tags) > 1
