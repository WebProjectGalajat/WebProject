@when(u'I modify song "{song}"')
def stem_impl(context, song):
    context.browser.get(context.get_url("/songs"))
    div = context.browser.find_element_by_id("content")
    for li in div.find_elements_by_tag_name("li"):
        song_name = li.text
        print(song_name)


@then(u'I\'m viewing the modified song "{song}"')
def step_impl(context, song):
    raise NotImplementedError(u'STEP: Then I\'m viewing the modified song')
