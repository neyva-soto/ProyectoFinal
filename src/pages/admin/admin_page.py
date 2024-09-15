from src.pages.base_page import BasePage
from src.pages.admin.admin_page_locators import AdminPageLocators
from src.pages.login.login_page_locators import LoginPageLocators


class AdminPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def isVisibleTitleAdmin(self):
        loop = self.context.async_context.loop
        loop.run_until_complete(self.context.page.query_selector(AdminPageLocators.TITLE_ADMIN))

    def goAdminSection(self):
        loop = self.context.async_context.loop
        loop.run_until_complete(self.find_element(AdminPageLocators.ADMIN_BUTTON).click())

    def goToSection(self, button_name):
        loop = self.context.async_context.loop
        loop.run_until_complete(self.find_element(AdminPageLocators.ANY_BUTTON_WITH_SPAN.format(button_name)).click())

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

