import os
import logging
from dotenv import load_dotenv

load_dotenv()


def get_env_variable(key, default=None):
    return os.getenv(key, default)


def get_log_level():
    log_level_str = get_env_variable('LOG_LEVEL', 'INFO').upper()
    return getattr(logging, log_level_str, logging.INFO)


def get_username():
    return get_env_variable('USERNAME_ORANGE', '')


def get_password():
    return get_env_variable('PASSWORD_ORANGE', '')
