import logging
import random
import re

from assertpy import assert_that
from behave import given, when, then

from src.pages.common.common_locators import CommonLocators
from src.pages.directory.directory_page_locators import DirectoryPageLocators

logger = logging.getLogger('framework')


@then(u'Records Found should be shown')
def step_impl(context):
    directory_page = context.current_page
    records_found_txt = directory_page.records_found_text(DirectoryPageLocators.RECORDS_FOUND)
    assert_that(records_found_txt).contains("Found")
