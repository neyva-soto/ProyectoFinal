import logging

from assertpy import assert_that
from behave import given, when, then

from src.pages.common.common_locators import CommonLocators
from src.utils.url_handler import get_url_for_page

logger = logging.getLogger('framework')


@given(u'The user is on the {page_name} Page')
def step_open_jobs_title_page(context, page_name):
    current_page = context.current_page
    url = get_url_for_page(page_name)
    current_page.open_page(url)
    current_url = current_page.get_url()
    if "login" in current_url and page_name not in ("Login", "login"):
        logger.debug("Redirected to login page, trying to login...")
        current_page.login()


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
