from src.pages.base_page import BasePage
from src.pages.login.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def login_button_click(self):
        loop = self.context.async_context.loop
        login_button = self.find_element(LoginPageLocators.LOGIN_BUTTON)
        loop.run_until_complete(login_button.click())
        return login_button

    def get_summary_text(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.find_element(LoginPageLocators.SUMMARY).inner_text())

    def set_search_user_input(self, search_input):
        loop = self.context.async_context.loop
        loop.run_until_complete(self.context.page.type(LoginPageLocators.USERNAME_INPUT, search_input))

    def set_search_pass_input(self, search_input):
        loop = self.context.async_context.loop
        loop.run_until_complete(self.context.page.type(LoginPageLocators.PASSWORD_INPUT, search_input))

    def get_dashboard_text(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.find_element(LoginPageLocators.DASHBOARD_TITLE).inner_text())

    def verify_input_field(self, input_name):
        loop = self.context.async_context.loop
        selector = LoginPageLocators.INPUT_FIELD_BY_NAME.format(input_name)
        print(selector)
        element = self.context.page.query_selector(selector)
        print(element)
        return loop.run_until_complete(element)

    def verify_user_input_required(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.query_selector(LoginPageLocators.WARNING_USER_INPUT))

    def verify_password_input_required(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.query_selector(LoginPageLocators.WARNING_PASSWORD_INPUT))

    def verify_display_button(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.query_selector(LoginPageLocators.LOGIN_BUTTON))

    def verify_display_warning(self):
        loop = self.context.async_context.loop
        warning_element = loop.run_until_complete(self.context.page.wait_for_selector(LoginPageLocators.INVALID_CREDENTIAL))
        return loop.run_until_complete(warning_element.inner_text())

    def click_forgot_password(self):
        loop = self.context.async_context.loop
        forgot_password_button = self.find_element(LoginPageLocators.FORGOT_PASSWORD)
        loop.run_until_complete(forgot_password_button.click())
        return forgot_password_button

    def verify_form_forgot_password(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.wait_for_selector(LoginPageLocators.FORM_FORGOT))

    def verify_field_password(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.query_selector(LoginPageLocators.FIELD_PASSWORD))

    def click_link_orange(self):
        loop = self.context.async_context.loop
        link_orange = self.find_element(LoginPageLocators.LINK_ORANGE)

        async def wait_for_new_page():
            async with self.context.page.expect_popup() as popup_info:
                await link_orange.click()
            return await popup_info.value
        return loop.run_until_complete(wait_for_new_page())

    def verify_page_orange(self):
        loop = self.context.async_context.loop
        pages = self.context.browser.contexts[0].pages
        if len(pages) == 2:
            loop.run_until_complete(pages[1].wait_for_load_state('load'))
            orange_home_slider = loop.run_until_complete(pages[1].query_selector(LoginPageLocators.PAGE_ORANGE))
            pages[1].close()
            return orange_home_slider

    def verify_empty_space(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.query_selector(LoginPageLocators.LOGIN_BUTTON))

    def get_input_text(self, locator):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.locator(locator).input_value())
