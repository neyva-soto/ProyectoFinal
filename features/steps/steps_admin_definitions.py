from assertpy import assert_that
from behave import given, when, then

from src.pages.admin.admin_page import AdminPage

@given(u'The user is logged in')
def user_logged_in(context):
    admin_page = context.current_page
    admin_page.login()

@given(u'The user is on the admin page')
def user_logged_in(context):
    admin_page = context.current_page
    admin_page.goAdminSection()

@given(u'that the user is inside the application')
def that_the_user_is_inside_the_application(context):
    admin_page = context.current_page
    #admin_page.open()
    admin_page.isVisibleTitleAdmin()

@when(u'The user clicks on the {button_name} button')
def the_user_clicks_on_the_Admin_button(context, button_name):
    admin_page = context.current_page
    admin_page.goToSection(button_name)

@then(u'the user will be redirected to admin section')
def the_user_will_be_redirected_to_admin_section(context):
    admin_page = context.current_page
    assert_that(admin_page.verifySectionSelected())
