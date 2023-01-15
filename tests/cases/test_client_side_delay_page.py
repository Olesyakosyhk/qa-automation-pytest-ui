import allure

from pages import Pages


class TestClientSideDelayPage:
    def test_client_side_delay_positive(
            self,
            playground_page: Pages,
    ):
        with allure.step('Переход на страницу "client_side_delay"'):
            playground_page.client_side_delay_page.go_to_page()

        with allure.step('Нажатие на кнопку'):
            playground_page.client_side_delay_page.click_blue_btn()

        with allure.step('Проверка ожидания появления текста метки'):
            assert playground_page.client_side_delay_page.check_label_text_is_present()
