import allure
import pytest

from pages import PlaygroundPage


@pytest.fixture()
def go_to_main_page(playground_page: PlaygroundPage) -> None:
    with allure.step('Переход на страницу площадки для UI Test'):
        playground_page.main_page.go_to_playground_page()


@pytest.fixture()
def go_to_class_attribute_page(playground_page: PlaygroundPage) -> None:
    with allure.step('Переход на страницу "class_attribute"'):
        playground_page.main_page.go_to_class_attribute_page()


@pytest.fixture()
def go_to_hidden_layers_page(playground_page: PlaygroundPage) -> None:
    with allure.step('Переход на страницу "hidden_layers"'):
        playground_page.main_page.go_to_hidden_layers_page()
