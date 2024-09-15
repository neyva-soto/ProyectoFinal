import logging

from src.pages.base_page import BasePage
from src.pages.admin.admin_page_locators import AdminPageLocators
from src.pages.login.login_page_locators import LoginPageLocators
from src.pages.usermanagement import user_management_page_locators
from src.pages.usermanagement.user_management_page_locators import UserManagementPageLocators


class UserManagementPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)
        self.logger = logging.getLogger("framework")

    def isVisibleTitleAdmin(self):
        loop = self.context.async_context.loop
        loop.run_until_complete(self.context.page.query_selector(AdminPageLocators.TITLE_ADMIN))

    def goAdminSection(self):
        loop = self.context.async_context.loop
        loop.run_until_complete(self.find_element(AdminPageLocators.ADMIN_BUTTON).click())

    def goToSection(self, button_name):
        loop = self.context.async_context.loop
        loop.run_until_complete(self.find_element(AdminPageLocators.ANY_BUTTON_WITH_SPAN.format(button_name)).click())

    def goToSort(self, button_sort):
        loop = self.context.async_context.loop
        # Encuentra el contenedor que tiene el texto "Username"
        header_cell = self.find_element(AdminPageLocators.CELL_HEADER)
        # Dentro de ese contenedor, encuentra el icono <i>
        print(header_cell)
        sort_icon = header_cell.locator(AdminPageLocators.BUTTON_SORT)
        self.logger.debug(sort_icon)
        loop.run_until_complete(sort_icon.click())

    def goToUp(self, button_up):
        loop = self.context.async_context.loop
        loop.run_until_complete(self.find_element(AdminPageLocators.BUTTON_UP.format(button_up)).click())

    def verifySectionSelected(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.locator(AdminPageLocators.BUTTON_SELECTED).is_visible())

    def login(self):
        loop = self.context.async_context.loop
        login_url = self.context.config.userdata.get("applicationUrl",
                                                      "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        loop.run_until_complete(self.context.page.goto(login_url))
        loop.run_until_complete(self.context.page.type(LoginPageLocators.USERNAME_INPUT, "Admin"))
        loop.run_until_complete(self.context.page.type(LoginPageLocators.PASSWORD_INPUT, "admin123"))
        login_button = self.find_element(LoginPageLocators.LOGIN_BUTTON)
        loop.run_until_complete(login_button.click())

    def get_title_text(self, locator):
        loop = self.context.async_context.loop
        loop.run_until_complete(self.context.page.wait_for_selector(locator))
        element_title = loop.run_until_complete(self.context.page.query_selector(locator))
        title = loop.run_until_complete(element_title.inner_text())
        self.logger.debug(f"get title return {title}")
        return title

    def search_bar(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.locator(UserManagementPageLocators.SEARCH_BAR).is_visible())

    def button_new_user(self):
        loop = self.context.async_context.loop
        return self.find_element(UserManagementPageLocators.BUTTON_NEW_USER)
        # return loop.run_until_complete(self.context.page.locator(UserManagementPageLocators.BUTTON_NEW_USER))

    def click_on_element(self, element):
        loop = self.context.async_context.loop
        return loop.run_until_complete(element.click())

    def clicks_on_first_element(self, locator):
        loop = self.context.async_context.loop
        elements = self.find_element(locator).first
        loop.run_until_complete(elements.click())

    def clicks_on_second_element(self, locator):
        loop = self.context.async_context.loop
        elements = self.find_element(locator).nth(1)
        loop.run_until_complete(elements.click())

    def goNewUserSection(self):
        loop = self.context.async_context.loop
        loop.run_until_complete(self.find_element(UserManagementPageLocators.PAGE_NEW_USER).click())

    def type_text_to_input_text(self, locator, input_text):
        element = self.find_element(locator)
        input_field = element.locator('input').nth(0)
        self.loop.run_until_complete(input_field.fill(input_text))
