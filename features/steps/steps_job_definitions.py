import logging
import random
import re

from assertpy import assert_that
from behave import given, when, then

from src.pages.common.common_locators import CommonLocators
from src.pages.jobs.jobs_page_locators import JobsPageLocators

logger = logging.getLogger('framework')


@then(u'Records must be shown for {page_title}')
def step_impl(context, page_title):
    jobs_page = context.current_page
    records_found_txt = jobs_page.get_text_from_element(JobsPageLocators.RECORDS_FOUND)
    match = re.search(r'\d+', records_found_txt)
    assert_that(match).is_not_none()


@then(u'User should see the error message "{error_message}"')
def step_impl(context, error_message):
    jobs_page = context.current_page
    text = jobs_page.get_text_from_element(JobsPageLocators.ERROR_MESSAGE)
    assert_that(text).is_not_none()
    assert_that(text).is_equal_to(error_message)


@when(u'User types "{user_input}" in {field_name} Field')
def step_impl(context, user_input, field_name):
    context.random_number = random.randint(10000, 50000)
    user_input = user_input.replace("<random>", str(context.random_number))
    current_page = context.current_page
    locator = JobsPageLocators.INPUT_FIELD_SPACE.format(field_name)
    current_page.type_text_to_input_text(locator, user_input)


@then(u'User should see the entry "{user_input}" in the page')
def step_impl(context, user_input):
    user_input = user_input.replace("<random>", str(context.random_number))
    current_page = context.current_page
    text = current_page.get_text_from_element(CommonLocators.ELEMENT_BY_TEXT.format(user_input))
    assert_that(text).is_not_none()


@when(u'User clicks on icon {icon_name} for "{user_input}"')
def step_impl(context, icon_name, user_input):
    user_input = user_input.replace("<random>", str(context.random_number))
    current_page = context.current_page
    locator = JobsPageLocators.INDIVIDUAL_JOB_TITLE_SPACE.format(user_input)
    current_page.click_icon_button(locator, icon_name)


@then(u'User should not see the entry "{user_input}" in the page')
def step_impl(context, user_input):
    user_input = user_input.replace("<random>", str(context.random_number))
    current_page = context.current_page
    element = current_page.exist_element(CommonLocators.ELEMENT_BY_TEXT.format(user_input))
    assert_that(element).is_none()
