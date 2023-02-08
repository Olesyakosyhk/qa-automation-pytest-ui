import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from app.pages import Pages


__all__ = [
    'playground_page',
]


@pytest.fixture()
def playground_page(browser: WebDriver) -> Pages:
    return Pages(browser)
