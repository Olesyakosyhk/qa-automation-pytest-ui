import allure

from pages import PlaygroundPage


class TestLoadDelay:
    def test_load_delay_positive(
            self,
            playground_page: PlaygroundPage,
            go_to_main_page,
    ):
        with allure.step('Переход на страницу "load_delay"'):
            playground_page.main_page.click_load_delay_btn()

        with allure.step('Проверка наличия кликабельной кнопки на странице "load_delay"'):
            assert playground_page.load_delay.check_btn_is_present()

    def test_load_delay_url(
            self,
            playground_page: PlaygroundPage,
            go_to_main_page,
    ):
        with allure.step('Переход на страницу "load_delay"'):
            playground_page.main_page.click_load_delay_btn()

        with allure.step('Проверка url на странице "load_delay"'):
            assert playground_page.load_delay.check_load_delay_url()
