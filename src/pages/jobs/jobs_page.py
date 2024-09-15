import logging

from src.pages.base_page import BasePage
from src.pages.jobs.jobs_page_locators import JobsPageLocators


class JobsPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)
        self.logger = logging.getLogger("framework")
        self.loop = self.context.async_context.loop

    def get_title(self):
        title = self.context.page.title()
        return self.loop.run_until_complete(title)

    def type_text_to_input_text(self, locator, input_text):
        element = self.find_element(locator)
        input_field = element.locator('input')
        self.loop.run_until_complete(input_field.fill(input_text))

    def click_icon_button(self, locator, icon_name):
        element = self.find_element(locator)
        if icon_name == 'edit':
            button_locator = JobsPageLocators.EDIT_BUTTON
        elif icon_name == 'delete':
            button_locator = JobsPageLocators.DELETE_BUTTON
        else:
            button_locator = ''
        icon_button = element.locator(button_locator)
        self.loop.run_until_complete(icon_button.click())

    def exist_element(self, locator):
        self.logger.debug(f"Gets an element using locator {locator}")
        try:
            return self.loop.run_until_complete(self.context.page.locator(locator).inner_text(timeout=1000))
        except:
            return
