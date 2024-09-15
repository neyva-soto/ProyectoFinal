from src.pages.base_page import BasePage
from src.pages.directory.directory_page_locators import DirectoryPageLocators


class DirectoryPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)
        self.loop = self.context.async_context.loop

    def records_found_text(self, selector):
        element = self.find_element(selector)
        return self.loop.run_until_complete(element.inner_text())

