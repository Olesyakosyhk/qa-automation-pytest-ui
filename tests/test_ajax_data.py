import allure

from pages import PlaygroundPage


class TestAJAXData:
    def test_ajax_data_positive(
            self,
            playground_page: PlaygroundPage,
            go_to_main_page,
    ):

        with allure.step('Переход на страницу "ajax"'):
            playground_page.main_page.click_ajax_data_btn()

        with allure.step('Проверка url страницы "ajax"'):
            assert playground_page.ajax_data.check_ajax_url()

        with allure.step('Нажатие на кнопку "TRIGGERING_AJAX_REQUEST"'):
            playground_page.ajax_data.click_triggering_ajax_request_btn()

        with allure.step('Проверка лейбла'):
            assert playground_page.ajax_data.check_label_is_present()
