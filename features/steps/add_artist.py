from selenium.webdriver import ActionChains

@when(u'I type an artist "{artist}"')
def step_impl(context, artist):
    context.browser.get(context.get_url('/artists/add/'))
    form = context.browser.find_element_by_tag_name('form')
    name_box = form.find_element_by_id('id_name')
    name_box.send_keys(artist)
    context.artist = artist
    description_box = form.find_element_by_id('id_description')
    description_box.send_keys('Descripcio original')
    submit_button = form.find_elements_by_tag_name('input')[-1]
    ActionChains(context.browser).click(submit_button).perform()



@then(u'I\'m viewing the artist details containing')
def step_impl(context):
    divs = context.browser.find_elements_by_tag_name('div')
    for div in divs:
        if div.id == "content":
            title_tag = content.find_element_by_tag_name('h1')
            title = title_tag.text
            assert title == context.artist
