import logging

from src.pages.login.login_page_locators import LoginPageLocators
from src.utils import dot_env_handler


class BasePage(object):

    def __init__(self, context):
        self.context = context
        self.loop = self.context.async_context.loop
        self.logger = logging.getLogger("framework")

    def find_element(self, locator):
        self.logger.debug(f"Gets an element using locator {locator}")
        return self.context.page.locator(locator)

    def clicks_on_element(self, locator):
        element = self.find_element(locator)
        self.logger.debug(f"Clicks on an element using locator {locator}")
        self.loop.run_until_complete(element.click())

    def get_text_from_element(self, locator):
        element = self.find_element(locator)
        if element:
            return self.loop.run_until_complete(element.inner_text())

    def open_page(self, url):
        self.loop.run_until_complete(self.context.page.goto(url))

    def get_url(self):
        return self.context.page.url

    def login(self):
        user_type = self.loop.run_until_complete(self.context.page.type(LoginPageLocators.USERNAME_INPUT, dot_env_handler.get_username()))
        pass_type = self.loop.run_until_complete(self.context.page.type(LoginPageLocators.PASSWORD_INPUT, dot_env_handler.get_password()))
        login_button = self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.loop.run_until_complete(login_button.click())

