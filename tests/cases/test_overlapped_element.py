import allure
from faker import Faker

from pages import PlaygroundPage


class TestOverlappedElement:
    def test_overlapped_element_positive(
            self,
            playground_page: PlaygroundPage,
            fake: Faker,
    ):
        with allure.step('Переход на страницу "overlapped_element"'):
            playground_page.main_page.go_to_page(name_page='overlapped_element')

        with allure.step('Ввести в поле "id" номер id'):
            playground_page.overlapped_element.set_id(str(fake.ssn()))

        with allure.step('Проскроллить до поля "Name"'):
            playground_page.overlapped_element.scroll_to_name_input()

        with allure.step('Ввести в поле "Name" имя'):
            playground_page.overlapped_element.set_name(str(fake.name()))
