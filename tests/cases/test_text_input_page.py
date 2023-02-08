import allure
import pytest
from faker import Faker

from app.pages import Pages


@allure.parent_suite('REGRESSION')
@allure.suite('TextInputPage')
@pytest.mark.regression
@pytest.mark.text_input_page
class TestTextInputPage:

    @allure.title('Тест №8 для страницы "text_input".')
    @allure.description('Поверить новое название синей кнопки')
    def test_text_input_btn(
            self,
            playground_page: Pages,
            fake: Faker,
    ):
        with allure.step('Переход на страницу "text_input"'):
            playground_page.text_input_page.text_input_page_url.go_to_page_by_url()

        with allure.step('Поверить кастомное название синей кнопки'):
            assert playground_page.text_input_page.check_default_text_blue_btn()

        new_text = fake.name()

        with allure.step(f'Ввести новое имя кнопки {new_text}'):
            playground_page.text_input_page.input_name.set_text(text=new_text)

        with allure.step('Нажать синюю кнопку'):
            playground_page.text_input_page.blue_button.click()

        with allure.step(f'Поверить новое название {new_text} синей кнопки'):
            assert playground_page.text_input_page.blue_button.check_text(text=new_text)
