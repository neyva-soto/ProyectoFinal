import logging
import random
import re

from assertpy import assert_that
from behave import given, when, then

from src.pages.common.common_locators import CommonLocators
from src.pages.candidates.candidates_page_locators import CandidatesPageLocators

logger = logging.getLogger('framework')


@when(u'The user type "{value}" for the email')
def step_impl(context, value):
    candidates_page = context.current_page
    candidates_page.type_text_to_input_for_email(value)


@when(u'The user click on the edit checkbox')
def step_impl(context):
    candidates_page = context.current_page
    candidates_page.click_on_edit_checkbox()


@when(u'The user type "{candidate_name}" for the candidate name field')
def step_impl(context, candidate_name):
    candidates_page = context.current_page
    candidates_page.type_text_to_input_for_candidate_name(candidate_name)


@when(u'The user clicks on the "{candidate_name}" dropdown option')
def step_impl(context, candidate_name):
    candidates_page = context.current_page
    candidates_page.click_on_custom_dropdown(candidate_name)



