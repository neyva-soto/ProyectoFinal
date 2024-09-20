from src.pages.base_page import BasePage
from src.pages.candidates.candidates_page_locators import CandidatesPageLocators
from src.pages.common.common_locators import CommonLocators


class CandidatesPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def type_text_to_input_for_email(self, input_text):
        input_fields = self.find_element(CandidatesPageLocators.INPUT_FIELDS_WITHOUT_NAME)
        self.loop.run_until_complete(input_fields.nth(1).fill(input_text))

    def click_on_edit_checkbox(self):
        element = self.find_element(CandidatesPageLocators.CHECKBOX_INPUT)
        self.loop.run_until_complete(element.nth(0).click())

    def type_text_to_input_for_candidate_name(self, candidate_name):
        input_fields = self.find_element(CandidatesPageLocators.INPUT_FIELDS_WITHOUT_NAME)
        self.loop.run_until_complete(input_fields.nth(1).fill(candidate_name))

    def click_on_custom_dropdown(self, candidate_name):
        dropdown_element = self.find_element(CandidatesPageLocators.AUTOCOMPLETE_DROPDOWN_BY_TEXT.format(candidate_name))
        element = dropdown_element.locator(CommonLocators.ELEMENT_BY_TEXT.format(candidate_name))
        self.loop.run_until_complete(element.first.click())
