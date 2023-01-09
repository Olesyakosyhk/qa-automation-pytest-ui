import allure
import pytest

from pages import PlaygroundPage


@pytest.fixture()
def go_to_main_page(playground_page: PlaygroundPage) -> None:
    with allure.step('Переход на страницу площадки для UI Test'):
        playground_page.main_page.go_to_playground_page()
