import logging
import random
import re

from assertpy import assert_that
from behave import given, when, then

from src.pages.common.common_locators import CommonLocators
from src.pages.vacancies.vacancies_page_locators import VacanciesPageLocators

logger = logging.getLogger('framework')


@when(u'The user type "{value}" for Vacancy Name')
def step_impl(context, value):
    context.random_number = random.randint(10000, 50000)
    user_input = value.replace("<random>", str(context.random_number))
    candidates_page = context.current_page
    candidates_page.type_text_to_input_for_vacancy_name(user_input)


@when(u'The user type "{value}" for Hiring Manager')
def step_impl(context, value):
    candidates_page = context.current_page
    candidates_page.type_text_to_input_for_hiring_manager(value)


@when(u'The user selects "{item}" option from Job Title dropdown')
def step_impl(context, item):
    candidates_page = context.current_page
    candidates_page.select_element_from_job_title_dropdown(item)


@when(u'The user selects "{item}" option from Job Title dropdown in vacancies view')
def step_impl(context, item):
    candidates_page = context.current_page
    candidates_page.select_element_from_job_title_dropdown(item, nth=0)


@when(u'The user selects "{item}" option from Status dropdown in vacancies view')
def step_impl(context, item):
    candidates_page = context.current_page
    candidates_page.select_element_from_job_title_dropdown(item, nth=3)
