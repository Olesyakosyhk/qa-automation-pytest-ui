import pytest

from pages import PlaygroundPage


@pytest.fixture()
def playground_page(browser) -> PlaygroundPage:
    yield PlaygroundPage(browser)
