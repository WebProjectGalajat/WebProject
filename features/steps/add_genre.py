from selenium.webdriver import ActionChains


@when(u'I type a genre')
def step_impl(context, genre):
    context.browser.get(context.get_url(''))  # Falta la URL
    form = context.browser.find_element_by_tag_name('form')
    name_box = form.find_element_by_id('id_genre')
    name_box.send_keys(genre)
    context.genre = genre
    description_box = form.find_element_by_id('id_description')
    description_box.send_keys('Descripcio original')
    submit_button = form.find_element_by_tag_name('input')[-1]
    ActionChains(context.browser).click(submit_button).perform()


@then(u'the list contains 1 genre')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the list contains 1 genre')
