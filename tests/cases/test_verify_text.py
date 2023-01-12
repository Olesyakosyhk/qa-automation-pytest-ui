import allure

from pages import PlaygroundPage


class TestVerifyText:

    def test_verify_text_positive(
            self,
            playground_page: PlaygroundPage,

    ):
        with allure.step('Переход на страницу "verify_text"'):
            playground_page.main_page.go_to_page(name_page='verify_text')

        with allure.step('Проверка соответствия текста приветствия на странице'):
            assert playground_page.verify_text.check_finds_an_element()
