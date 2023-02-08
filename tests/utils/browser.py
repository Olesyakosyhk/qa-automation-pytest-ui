from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from core.settings import CHROME_VERSION, FIREFOX_VERSION
from core_ui.resources.strings import BROWSER_NAME_TYPE


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
