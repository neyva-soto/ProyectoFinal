import time

from src.pages.base_page import BasePage
from src.pages.candidates.candidates_page_locators import CandidatesPageLocators
from src.pages.vacancies.vacancies_page_locators import VacanciesPageLocators
from src.pages.common.common_locators import CommonLocators


class VacanciesPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def type_text_to_input_for_vacancy_name(self, value):
        element = self.find_element(VacanciesPageLocators.INPUT_FIELDS_WITHOUT_NAME)
        self.loop.run_until_complete(element.nth(1).fill(value))

    def type_text_to_input_for_hiring_manager(self, value):
        element = self.find_element(VacanciesPageLocators.INPUT_FIELDS_WITHOUT_NAME)
        self.loop.run_until_complete(element.nth(2).fill(value))

    def select_element_from_job_title_dropdown(self, value, nth=0):
        element = self.find_element(VacanciesPageLocators.DROPDOWN_BUTTON).nth(nth)
        element = element.locator("i")
        self.loop.run_until_complete(element.click())
        # import time
        # time.sleep(3)
        # element2 = self.find_element(".oxd-select-dropdown")
        # text_html = self.loop.run_until_complete(element2.evaluate("element => element.outerHTML"))
        # print(text_html)
        # raise
        item = self.find_element(VacanciesPageLocators.SELECT_OPTION_BY_TEXT.format(value))
        text_html = self.loop.run_until_complete(item.first.evaluate("element => element.outerHTML"))
        print(text_html)
        self.loop.run_until_complete(item.first.click())

    # def click_on_first_element_in_custom_dropdown(self, hint):
    #     dropdown_element = self.find_element(CandidatesPageLocators.AUTOCOMPLETE_DROPDOWN_BY_TEXT.format(hint))
    #     elements = dropdown_element.locator(CommonLocators.ELEMENT_BY_TEXT.format(hint))
    #     self.loop.run_until_complete(elements.first.click())
