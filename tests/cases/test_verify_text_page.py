import allure

from pages import Pages


class TestVerifyTextPage:

    def test_verify_text_positive(
            self,
            playground_page: Pages,

    ):
        with allure.step('Переход на страницу "verify_text"'):
            playground_page.verify_text_page.go_to_page()

        with allure.step('Проверка соответствия текста приветствия на странице'):
            assert playground_page.verify_text_page.check_finds_an_element()
