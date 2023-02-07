import pytest

from app.pages import Pages


@pytest.fixture()
def playground_page(browser) -> Pages:
    return Pages(browser)
