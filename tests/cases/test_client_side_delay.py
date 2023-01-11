import allure

from pages import PlaygroundPage


class TestClientSideDelay:
    def test_client_side_delay_positive(
            self,
            playground_page: PlaygroundPage,
    ):
        with allure.step('Переход на страницу "client_side_delay"'):
            playground_page.main_page.go_to_page(name_page='client_side_delay')

        with allure.step('Нажатие на кнопку'):
            playground_page.common_methods.click_blue_btn()

        with allure.step('Проверка ожидания появления текста метки'):
            assert playground_page.client_side_delay.check_label_text_is_present()
