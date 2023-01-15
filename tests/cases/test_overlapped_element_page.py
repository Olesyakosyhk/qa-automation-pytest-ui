import allure
from faker import Faker

from pages import Pages


class TestOverlappedElementPage:
    def test_overlapped_element_positive(
            self,
            playground_page: Pages,
            fake: Faker,
    ):
        with allure.step('Переход на страницу "overlapped_element"'):
            playground_page.overlapped_element_page.go_to_page()

        with allure.step('Ввести в поле "id" номер id'):
            playground_page.overlapped_element_page.set_id(str(fake.ssn()))

        with allure.step('Проскроллить до поля "Name"'):
            playground_page.overlapped_element_page.scroll_to_name_input()

        with allure.step('Ввести в поле "Name" имя'):
            playground_page.overlapped_element_page.set_name(str(fake.name()))
