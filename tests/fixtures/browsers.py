from typing import Literal

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from core.settings import (
    CHROME_VERSION, FIREFOX_VERSION, INCLUDE_BROWSERS,
)


BROWSER_NAME_TYPE = Literal['chrome', 'firefox']


def get_browser_local(browser_name: BROWSER_NAME_TYPE) -> WebDriver:
    """
    Получить драйвер для манипуляцией браузером.

    :param browser_name: Название бразуера.
    :return: Драйвер браузера.
    """
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=2560,1440')

        browser = webdriver.Chrome(
            executable_path=ChromeDriverManager(version=CHROME_VERSION).install(),
            options=options,
        )
    else:
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=2560,1440')
        browser = webdriver.Firefox(
            executable_path=GeckoDriverManager(version=FIREFOX_VERSION).install(),
            options=options,
        )

    browser.implicitly_wait(15)

    return browser


@pytest.fixture(params=INCLUDE_BROWSERS, autouse=True)
def browser(request) -> WebDriver:
    """
    Получение экземпляра браузера.
    """
    browser_name = request.param

    browser = get_browser_local(browser_name=browser_name)

    yield browser

    browser.delete_all_cookies()
    browser.quit()
