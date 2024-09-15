import os
import logging
from src.utils.dot_env_handler import get_log_level

LOG_FORMAT = "%(asctime)s %(levelname)s %(filename)s:%(lineno)d - %(message)s"
LOG_LEVEL = get_log_level()


def setup_logger(log_file='allure-results/logs/execution.log'):
    log_file = os.path.abspath(log_file)
    log_dir = os.path.dirname(log_file)

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(LOG_LEVEL)
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    logger = logging.getLogger('framework')
    logger.setLevel(LOG_LEVEL)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.debug("Logging initialized")
