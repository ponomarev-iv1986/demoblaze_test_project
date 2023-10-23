import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://www.demoblaze.com'
    if config.settings.ENVIRONMENT == 'local':
        browser.config.window_width = 1400
        browser.config.window_height = 800
        options = webdriver.ChromeOptions()
        browser.config.driver_options = options
    else:
        options = Options()
        capabilities = {
            'browserName': 'chrome',
            'browserVersion': '100',
            'selenoid:options': {
                'enableVNC': True,
                'enableVideo': True
            }
        }
        options.capabilities.update(capabilities)

        login = config.settings.SELENOID_LOGIN
        password = config.settings.SELENOID_PASSWORD

        driver = webdriver.Remote(
            command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
            options=options
        )
        browser.config.driver = driver

    yield

    browser.quit()
