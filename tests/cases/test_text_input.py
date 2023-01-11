import allure
from faker import Faker

from pages import PlaygroundPage
from pages.common_methods import CommonMethods


class TestTextInput:
    def test_text_input_btn(
            self,
            playground_page: PlaygroundPage,
            fake: Faker,
    ):
        with allure.step('Переход на страницу "text_input"'):
            playground_page.main_page.go_to_page(name_page='text_input')

        with allure.step('Поверить кастомное название синей кнопки'):
            assert playground_page.text_input.check_name_blue_btn()

        with allure.step('Ввести новое имя кнопки'):
            new_name = fake.name()
            playground_page.text_input.input_name_for_btn(new_name=new_name)

        with allure.step('Нажать синюю кнопку'):
            playground_page.common_methods.click_blue_btn()

        with allure.step(f'Поверить новое название {new_name} синей кнопки'):
            assert playground_page.text_input.check_new_name_blue_btn(new_name=new_name)
