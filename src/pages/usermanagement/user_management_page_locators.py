class UserManagementPageLocators:
    TITLE_USERMANAGEMENT = ".oxd-topbar-body-nav-tab-item"
    USER_BUTTON = ".oxd-topbar-body-nav-tab-link"
    ANY_BUTTON_WITH_SPAN = "//a/span[text()='{}']"
    BUTTON_SELECTED = "//a[contains(@class,'active')]"
    TEXT_TITLE = "h5[data-v-7b563373][data-v-b4b62742]"
    GET_USERS = "text=Records Found"
    CELL_HEADER = "div.oxd-table-header-cell:has-text('Username')"
    BUTTON_SORT = "div.oxd-table-header-sort"
    BUTTON_UP = "span.oxd-text.oxd-text--span:text='Ascending'"
    SEARCH_BAR = ".oxd-grid-item .oxd-input-group .oxd-input"
    BUTTON_NEW_USER = 'button:has-text("Add")'
    PAGE_NEW_USER = "text='For a strong password, please use a hard to guess combination of text with upper and lower case characters, symbols and numbers'"
    BUTTON_DELETE = ".oxd-icon.bi-trash"
    BUTTON_PENCIL = ".oxd-icon.bi-pencil-fill"
    BUTTON_SEARCH_HIDDEN= ".oxd-icon.bi-caret-up-fill"
    INPUT_FIELD_SPACE = '.oxd-input-field-bottom-space:has-text("{}")'
    BUTTON_EXIT = ".oxd-dialog-close-button.oxd-dialog-close-button-position"
    BUTTON_SELECTION = ".oxd-checkbox-input.oxd-checkbox-input--active.--label-right.oxd-checkbox-input"