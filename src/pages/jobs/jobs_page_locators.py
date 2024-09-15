class JobsPageLocators:
    JOB_TITLE = ".orangehrm-main-title"
    ERROR_MESSAGE = ".oxd-input-field-error-message"
    RECORDS_FOUND = "text=Records Found"
    BUTTON_BY_TEXT = 'button:has-text("{}")'
    FORM_WITH_TEXT = 'form:has-text("{}")'
    INPUT_FIELD_BY_NAME_AND_TYPE = '.oxd-input-field-bottom-space:has-text("{}"):has({})'
    INPUT_FIELD_SPACE = '.oxd-input-field-bottom-space:has-text("{}")'
    TYPEABLE = 'input, textarea'
    INDIVIDUAL_JOB_TITLE_SPACE = '.oxd-table-card:has-text("{}")'
    EDIT_BUTTON = 'button:has(.bi-pencil-fill)'
    DELETE_BUTTON = 'button:has(.bi-trash)'
