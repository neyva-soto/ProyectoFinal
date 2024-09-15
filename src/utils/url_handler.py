import json
from urllib.parse import urljoin


class URLHandler:
    def __init__(self, config_file_path):
        self.config = self.load_config(config_file_path)
        self.base_url = self.config.get("BASE_URL")

    def load_config(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def construct_url(self, path):
        return urljoin(self.base_url, path)

    def get_url(self, section, key):
        path = self.config.get("ENDPOINTS", {}).get(section, {}).get(key)
        if self.base_url and path:
            return self.construct_url(path)
        else:
            raise ValueError(f"Invalid section or key '{section}.{key}' not found in the config.")


def get_url_for_page(page_name):
    page_name = page_name.lower()
    page_name = page_name.replace(' ', '_')
    parameters = url_parameters.get(page_name, ("AUTH", "LOGIN"))
    return url_handler.get_url(*parameters)


url_handler = URLHandler('src/assets/json_url_map.json')

url_parameters = {
    "login": ("AUTH", "LOGIN"),
    "user_management": ("ADMIN", "USER_MANAGEMENT"),
    "job_titles": ("ADMIN", "JOB_TITLES"),
    "pay_grades": ("ADMIN", "PAY_GRADES")
}

# Samples
# login_url = url_handler.get_url("AUTH", "LOGIN")
# user_management_url = url_handler.get_url("ADMIN", "USER_MANAGEMENT")
# job_titles_url = url_handler.get_url("ADMIN", "JOB_TITLES")
# pay_grades_url = url_handler.get_url("ADMIN", "PAY_GRADES")

