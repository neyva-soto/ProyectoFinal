import logging
import random
import re

from assertpy import assert_that
from behave import given, when, then

from src.pages.common.common_locators import CommonLocators
from src.pages.usermanagement.user_management_page import UserManagementPage
from src.pages.usermanagement.user_management_page_locators import UserManagementPageLocators

logger = logging.getLogger("framework")

# @given(u'The user is logged in')
# def user_logged_in(context):
#     admin_page = context.admin_page
#     admin_page.login()
#
# @given(u'The user is on the admin page')
# def user_logged_in(context):
#     admin_page = context.admin_page
#     admin_page.goAdminSection()
#
# @given(u'that the user is inside the application')
# def that_the_user_is_inside_the_application(context):
#     admin_page = context.current_page
#     #admin_page.open()
#     admin_page.isVisibleTitleAdmin()
#

#The user clicks on the up button
@then(u'The user is in User Management Section')
def the_user_is_user_management_section(context):
    user_management_page = context.current_page
    assert assert_that(user_management_page.get_title_text(UserManagementPageLocators.TEXT_TITLE)).is_equal_to("System Users")

@then(u'users must be displayed')
def users_must_be_displayed(context):
    user_management_page = context.current_page
    texto = user_management_page.get_title_text(UserManagementPageLocators.GET_USERS)
    digito_encontrado = re.search(r'\d', texto)
    logger.debug(f"digito encontrado {digito_encontrado}")
    assert assert_that(digito_encontrado).is_true()

@when(u'The user clicks on sort button')
def the_user_clicks_on_the_sort_button(context):
    user_management_page = context.current_page
    user_management_page.goToSort()

@when(u'The user clicks on up button')
def the_user_clicks_on_the_up_button(context):
    user_management_page = context.current_page
    user_management_page.goToUp()

@then(u'Will display the search bar')
def will_display_the_search_bar(context):
    user_management_page = context.current_page
    search_bar = user_management_page.search_bar()
    assert assert_that(search_bar).is_not_none()

@then (u'will display button create user')
def will_display_button_create_user(context):
    user_management_page = context.current_page
    button_user = user_management_page.button_new_user()
    assert assert_that(button_user).is_not_none()


@when(u'The user cliks on the add user button')
def the_user_cliks_on_the_add_user_button(context):
    user_management_page = context.current_page
    element = user_management_page.button_new_user()
    user_management_page.click_on_element(element)


@then(u'will display page add user section')
def will_display_page_add_user_section(context):
    user_management_page = context.current_page
    user_management_page.goNewUserSection()
    assert_that(user_management_page.verifySectionSelected()).is_not_none()


# @then(u'User should see button {button_text}')
# def step_impl(context, button_text):
#     user_management_page = context.current_page
#     element = user_management_page.find_element(CommonLocators.BUTTON_BY_TEXT.format(button_text))
#     assert_that(element).is_not_none()


# @when(u'User clicks on button {button_text}')
# def step_impl(context, button_text):
#     user_management_page = context.current_page
#     user_management_page.clicks_on_element(CommonLocators.BUTTON_BY_TEXT.format(button_text))
#
#
# @then(u'User should see a form with content {form_content_text}')
# def step_impl(context, form_content_text):
#     user_management_page = context.current_page
#     element = user_management_page.find_element(CommonLocators.FORM_WITH_TEXT.format(form_content_text))
#     assert_that(element).is_not_none()
#
#
# @then(u'User should see a {field_type} field for {field_name}')
# def step_impl(context, field_type, field_name):
#     user_management_page = context.current_page
#     locator = CommonLocators.INPUT_FIELD_BY_NAME_AND_TYPE.format(field_name, field_type)
#     element_found = user_management_page.find_element(locator)
#     assert_that(element_found).is_not_none()


@then(u'User should display button trash')
def step_impl(context):
    user_management_page = context.current_page
    element = user_management_page.find_element(CommonLocators.BUTTON_DELETE)
    assert_that(element).is_not_none()


@then(u'User should display button pencil')
def step_impl(context):
    user_management_page = context.current_page
    element = user_management_page.find_element(UserManagementPageLocators.BUTTON_PENCIL)
    assert_that(element).is_not_none()

@when(u'User clicks on icon delete')
def step_impl(context):
    user_management_page = context.current_page
    user_management_page.clicks_on_second_element(UserManagementPageLocators.BUTTON_DELETE)
@when(u'User clicks on icon edit')
def step_impl(context):
    user_management_page = context.current_page
    user_management_page.clicks_on_first_element(UserManagementPageLocators.BUTTON_PENCIL)

@when(u'User clicks on icon exit')
def step_impl(context):
    user_management_page = context.current_page
    user_management_page.clicks_on_first_element(UserManagementPageLocators.BUTTON_EXIT)

@when(u'User clicks icon selection')
def step_impl(context):
    user_management_page = context.current_page
    user_management_page.clicks_on_first_element(UserManagementPageLocators.BUTTON_SELECTION)

# @then(u'User display see button trash')
# def user_should_see_button_trash(context):
#     user_management_page = context.current_page
#     element = user_management_page.button_trash()
#     user_management_page.click_on_element(element)

@then(u'User should see "{element_text}" message in the page')
def step_impl(context, element_text):
    user_management_page = context.current_page
    element = user_management_page.find_element(CommonLocators.ELEMENT_BY_TEXT.format(element_text))
    assert_that(element).is_not_none()


@then(u'User should display button hidden')
def step_impl(context):
    user_management_page = context.current_page
    element = user_management_page.find_element(CommonLocators.BUTTON_SEARCH_HIDDEN)
    assert_that(element).is_not_none()


@when(u'User types text "{user_input}" in {field_name} Field')
def step_impl(context, user_input, field_name):
    context.random_number = random.randint(10000, 50000)
    user_input = user_input.replace("<random>", str(context.random_number))
    current_page = context.current_page
    locator = UserManagementPageLocators.INPUT_FIELD_SPACE.format(field_name)
    current_page.type_text_to_input_text(locator, user_input)


@then(u'User should see the user entry "{user_input}" in the page')
def step_impl(context, user_input):
    user_input = user_input.replace("<random>", str(context.random_number))
    current_page = context.current_page
    text = current_page.get_text_from_element(CommonLocators.ELEMENT_BY_TEXT.format(user_input))
    assert_that(text).is_not_none()
