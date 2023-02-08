import allure
import pytest
from faker import Faker

from app.pages import Pages


@allure.parent_suite('REGRESSION')
@allure.suite('OverlappedElementPage')
@pytest.mark.regression
@pytest.mark.overlapped_element_page
class TestOverlappedElementPage:

    @allure.title('Тест №17 для страницы "overlapped_element".')
    @allure.description('Ввести в поле "Name" имя')
    def test_overlapped_element_positive(
            self,
            playground_page: Pages,
            fake: Faker,
    ):
        with allure.step('Переход на страницу "overlapped_element"'):
            playground_page.overlapped_element_page.overlapped_page_url.go_to_page_by_url()

        with allure.step('Ввести в поле "id" номер id'):
            playground_page.overlapped_element_page.input_id.set_text(str(fake.ssn()))

        with allure.step('Проскроллить до поля "Name"'):
            playground_page.overlapped_element_page.scroll_page_to_element(
                element=playground_page.overlapped_element_page.input_name.element,
            )

        with allure.step('Ввести в поле "Name" имя'):
            playground_page.overlapped_element_page.input_name.set_text(str(fake.name()))
