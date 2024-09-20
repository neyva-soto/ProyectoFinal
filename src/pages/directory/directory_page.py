from src.pages.base_page import BasePage
from src.pages.directory.directory_page_locators import DirectoryPageLocators


class DirectoryPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)
        self.loop = self.context.async_context.loop

    def records_found_text(self, selector):
        element = self.find_element(selector)
        return self.loop.run_until_complete(element.inner_text())

    def click_on_drop_down_job_title(self, selector):
        element = self.find_element(selector)
        self.loop.run_until_complete(element.first.click())

    def click_on_drop_down_location(self, selector):
        element = self.find_element(selector)
        self.loop.run_until_complete(element.nth(1).click())

    def select_from_dropdown(self, item_name):
        element = self.loop.run_until_complete(self.context.page.query_selector(DirectoryPageLocators.DROPDOWN_LIST))
        # html_content = self.loop.run_until_complete(element.evaluate("element => element.outerHTML"))
        self.loop.run_until_complete(
            self.context.page.click(DirectoryPageLocators.DROPDOWN_OPTION.format(item_name))
        )
