import allure

from pages import Pages


class TestLoadDelayPage:
    def test_load_delay_positive(
            self,
            playground_page: Pages,
            go_to_main_page,
    ):
        with allure.step('Переход на страницу "load_delay"'):
            playground_page.main_page.click_load_delay_btn()

        with allure.step('Проверка наличия кликабельной кнопки на странице "load_delay"'):
            assert playground_page.load_delay_page.check_btn_is_present()

    def test_load_delay_url(
            self,
            playground_page: Pages,
            go_to_main_page,
    ):
        with allure.step('Переход на страницу "load_delay"'):
            playground_page.load_delay_page.go_to_page()

        with allure.step('Проверка url на странице "load_delay"'):
            assert playground_page.load_delay_page.check_url()
