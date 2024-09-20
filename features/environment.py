import os
import logging
from xml.etree.cElementTree import Element, SubElement, ElementTree

from src.pages.candidates.candidates_page import CandidatesPage
from src.utils.config_loader import playwright_config
from src.utils.logger_config import setup_logger

import allure
from allure_commons.types import AttachmentType
from behave.api.async_step import use_or_create_async_context
from behave.runner import Context
from playwright.async_api import async_playwright

from src.pages.admin.admin_page import AdminPage
from src.pages.login.login_page import LoginPage
from src.pages.jobs.jobs_page import JobsPage
from src.pages.usermanagement.user_management_page import UserManagementPage


def before_scenario(context: Context, scenario):
    use_or_create_async_context(context)
    loop = context.async_context.loop
    headless = playwright_config().getboolean('headless')
    context.playwright = loop.run_until_complete(async_playwright().start())
    context.browser = loop.run_until_complete(context.playwright.chromium.launch(headless=headless))
    context.page = loop.run_until_complete(context.browser.new_page())
    if 'login' in scenario.feature.tags:
        context.current_page = LoginPage(context)
    elif 'admin' in scenario.feature.tags:
        context.current_page = AdminPage(context)
    elif 'user_management' in scenario.feature.tags:
        context.current_page = UserManagementPage(context)
    elif 'jobs' in scenario.feature.tags:
        context.current_page = JobsPage(context)
    elif 'candidates' in scenario.feature.tags:
        context.current_page = CandidatesPage(context)
    else:
        raise ValueError(f"No page initialization defined for tags: {scenario.feature.tags}")


def after_scenario(context: Context, scenario):
    loop = context.async_context.loop

    if scenario.status == "failed":
        allure.attach(loop.run_until_complete(context.page.screenshot()), name="Screenshot",
                      attachment_type=AttachmentType.PNG)
    loop.run_until_complete(context.page.close())
    loop.run_until_complete(context.browser.close())


def configure_allure_reports(logger):
    logger.debug("Configuring Allure reports")
    allure_results_dir = os.path.join("./allure-results")
    os.makedirs(allure_results_dir, exist_ok=True)
    environment = Element("environment")
    for key, value in os.environ.items():
        param = SubElement(environment, "parameter")
        SubElement(param, "key").text = key
        SubElement(param, "value").text = value
    ElementTree(environment).write(os.path.join(allure_results_dir, "environment.xml"))


def before_all(context):
    setup_logger()
    logger = logging.getLogger('framework')
    configure_allure_reports(logger)
    logger.info("Starting Behave tests")


def after_all(context):
    logger = logging.getLogger('framework')
    logger.info("Finished Behave tests")
