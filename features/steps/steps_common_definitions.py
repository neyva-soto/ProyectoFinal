import logging

from assertpy import assert_that
from behave import given, when, then

from src.pages.common.common_locators import CommonLocators
from src.utils.url_handler import get_url_for_page

logger = logging.getLogger('framework')


@given(u'The user is on the {page_name} Page')
def step_open_page(context, page_name):
    current_page = context.current_page
    url = get_url_for_page(page_name)
    current_page.open_page(url)
    current_url = current_page.get_url()
    if "login" in current_url and page_name not in ("Login", "login"):
        logger.debug("Redirected to login page, trying to login...")
        current_page.login()

@when(u'The user navigates to {page_name} page')
def step_navigates_page(context, page_name):
    current_page = context.current_page
    url = get_url_for_page(page_name)
    current_page.open_page(url)


@then(u'User should see button {button_text}')
def step_impl(context, button_text):
    current_page = context.current_page
    element = current_page.find_element(CommonLocators.BUTTON_BY_TEXT.format(button_text))
    assert_that(element).is_not_none()


@when(u'User clicks on button {button_text}')
def step_impl(context, button_text):
    current_page = context.current_page
    current_page.clicks_on_element(CommonLocators.BUTTON_BY_TEXT.format(button_text))


@then(u'User should see a form with content {form_content_text}')
def step_impl(context, form_content_text):
    current_page = context.current_page
    element = current_page.find_element(CommonLocators.FORM_WITH_TEXT.format(form_content_text))
    assert_that(element).is_not_none()


@then(u'User should see a {field_type} field for {field_name}')
def step_impl(context, field_type, field_name):
    current_page = context.current_page
    locator = CommonLocators.INPUT_FIELD_BY_NAME_AND_TYPE.format(field_name, field_type)
    element_found = current_page.find_element(locator)
    assert_that(element_found).is_not_none()


@when(u'The user type "{value}" in the input field with name {field_name}')
def the_user_type_value_in_the_input_field(context, value, field_name):
    current_page = context.current_page
    current_page.type_text_to_input_text(CommonLocators.INPUT_FIELD_BY_NAME.format(field_name), value)


@then(u'User should see "{value}" text in the page')
def step_impl(context, value):
    current_page = context.current_page
    text = current_page.get_text_from_element(CommonLocators.ELEMENT_BY_TEXT.format(value))
    assert_that(text).contains(value)


@when(u'The user clicks on the "{icon_name}" icon for "{text_row}" row')
def step_impl(context, icon_name, text_row):
    current_page = context.current_page
    current_page.clicks_on_icon_in_row(icon_name, text_row)


@then(u'The user should see "{text_in_row}" card row')
def step_impl(context, text_in_row):
    current_page = context.current_page
    text = current_page.get_card_text_by_content(text_in_row)
    assert_that(text).contains(text_in_row)
