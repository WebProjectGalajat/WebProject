from behave import *


@when(u'I type a genre')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url(''))  # Falta ficar la URL
        if context.browser.url == context.get_url(
                ''):  # Falta ficar la URL (Aquesta i la anterior URL han de coincidir)
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()


@then(u'the list contains 1 genre')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the list contains 1 genre')
