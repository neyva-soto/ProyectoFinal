from assertpy import assert_that
from behave import given, when, then

from src.pages.login.login_page_locators import LoginPageLocators


@when(u'the user enters the value "{value}" in the text-input for username')
def the_user_enters_the_value_in_the_username_text_input(context, value):
    login_page = context.current_page
    login_page.set_search_user_input(value)


@when(u'the user enters the value "{value}" in the text-input for password')
def the_user_enters_the_value_in_the_password_text_input(context, value):
    login_page = context.current_page
    login_page.set_search_pass_input(value)


@when(u'the user clicks login button')
def the_user_clears_filters(context):
    login_page = context.current_page
    login_page.login_button_click()


@then(u'the user should see the following text in the page "{value}"')
def the_user_should_see_the_following_result_summary(context, value):
    login_page = context.current_page
    summary_text = login_page.get_dashboard_text()
    assert_that(summary_text).is_equal_to(value)


@then(u'I see input field in the page with id "{id_selector}"')
def step_the_user_should_see_the_field(context, id_selector):
    login_page = context.current_page
    login_page.get_summary_text()
    input_field = login_page.verify_input_field(id_selector)
    assert_that(input_field).is_not_none()


@then(u'Then it will be shown that the {input} field is required')
def then_it_will_be_shown_that_the_field_is_required(context, input):
    login_page = context.current_page
    if input == "username":
        assert_that(login_page.verify_user_input_required()).is_not_none()
    else:
        assert_that(login_page.verify_password_input_required()).is_not_none()


@then(u'button will be displayed')
def button_will_be_displayed(context):
    login_page = context.current_page
    login_page.get_summary_text()
    assert assert_that(login_page.verify_display_button()).is_not_none()


@then(u'User and password fields should be displayed are required')
def user_and_password_fields_will_be_displayed(context):
    login_page = context.current_page
    assert_that(login_page.verify_user_input_required()).is_not_none()
    assert_that(login_page.verify_password_input_required()).is_not_none()


@then(u'will display a message')
def will_display_a_message(context):
    login_page = context.current_page
    assert_that(login_page.verify_display_warning()).is_not_none()


@then(u'will display the error message "{message}"')
def will_display_an_error_message(context, message):
    login_page = context.current_page
    warning_text = login_page.verify_display_warning()
    assert_that(warning_text).is_equal_to(message)


@when(u'the user clicks in forgotPassword')
def the_user_clicks_in_forgot_password(context):
    login_page = context.current_page
    assert_that(login_page.click_forgot_password())


@then(u'the new password form will show up')
def the_new_password_form_will_show_up(context):
    login_page = context.current_page
    assert assert_that(login_page.verify_form_forgot_password()).is_not_none()


@when(u'the user clicks in linkOrange')
def the_user_clicks_in_link_orange(context):
    login_page = context.current_page
    login_page.click_link_orange()


@then(u'the password field must be hidden')
def the_password_field_must_be_hidden(context):
    login_page = context.current_page
    assert assert_that(login_page.verify_field_password())


@then(u'the will see new page linkOrange')
def the_will_see_new_page_link_orange(context):
    login_page = context.current_page
    assert assert_that(login_page.verify_page_orange()).is_not_none()


@then(u'will display the page empty spaces')
def will_display_the_page_empty_spaces(context):
    login_page = context.current_page
    assert assert_that(login_page.verify_empty_space()).is_not_none()


@then(u'will display text-input for username empty')
def will_display_text_input_for_username_empty(context):
    login_page = context.current_page
    assert assert_that(login_page.get_input_text(LoginPageLocators.USERNAME_INPUT)).is_equal_to("")


@then(u'will display text-input for password empty')
def will_display_text_input_for_password_empty(context):
    login_page = context.current_page
    assert assert_that(login_page.get_input_text(LoginPageLocators.PASSWORD_INPUT)).is_equal_to("")
