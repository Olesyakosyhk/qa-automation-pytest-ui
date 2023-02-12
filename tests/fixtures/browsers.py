import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from core.settings import INCLUDE_BROWSERS
from tests.utils.browser import get_browser_local


__all__ = [
    'browser',
]


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
