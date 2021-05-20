@when(u'I delete an artist "{artist}"')
def step_impl(context, artist):
    # From the artist list, enter to delete the song
    context.browser.get(context.get_url("/artists"))
    div = context.browser.find_element_by_id("content")
    for li in div.find_elements_by_tag_name("li"):
        # If we are in the correct link, click
        if artist in li.text:
            li.find_element_by_tag_name("a").click()
            break
    # Check if the URL is correct
    assert context.browser.current_url.rstrip("/").split("/")[-2] == "artists"
    artist_id = context.browser.current_url.rstrip("/").split("/")[-1]
    try:
        int(artist_id)
    except ValueError:
        raise
    # We are in the correct URL
    links = context.browser.find_elements_by_tag_name("a")
    for link in links:
        if "Delete" in link.text:
            link.click()
            break
    assert context.browser.current_url.rstrip("/").split("/")[-1] == "artists"


@then(u'I\'m viewing a list without artist "{artist}"')
def step_impl(context, artist):
    assert context.browser.current_url.rstrip("/").split("/")[-1] == "artists"
    div = context.browser.find_element_by_id('content')
    for li in div.find_elements_by_tag_name("li"):
        if artist in li.text:
            raise
