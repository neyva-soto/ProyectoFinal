class CommonLocators:
    ELEMENT_BY_TEXT = "text={}"
    BUTTON_BY_TEXT = 'button:has-text("{}")'
    FORM_WITH_TEXT = 'form:has-text("{}")'
    INPUT_FIELD_BY_NAME_AND_TYPE = '.oxd-input-field-bottom-space:has-text("{}"):has({})'
    INPUT_FIELD_BY_NAME = 'input[name="{}"]'
    TABLE_CARD_BY_TEXT = '.oxd-table-card:has-text("{}")'
    AUTOCOMPLETE_DROPDOWN_BY_TEXT = '.oxd-autocomplete-dropdown:has(.oxd-autocomplete-option):not(:has-text("Searching....")):has-text("{}")'
    AUTOCOMPLETE_DROPDOWN_OPTION_BY_TEXT = '.oxd-autocomplete-option:has-text("{}")'
