import configparser


def playwright_config(file_path='test_config.ini'):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config['playwright']
