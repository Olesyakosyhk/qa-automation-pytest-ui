import allure

from pages import Pages


class TestAJAXDataPage:
    def test_ajax_data_positive(
            self,
            playground_page: Pages,
            go_to_main_page,
    ):

        with allure.step('Переход на страницу "ajax"'):
            playground_page.ajax_data_page.go_to_page()

        with allure.step('Проверка url страницы "ajax"'):
            assert playground_page.ajax_data_page.check_url()

        with allure.step('Нажать на синюю кнопку'):
            playground_page.ajax_data_page.click_blue_btn()

        with allure.step('Проверка лейбла'):
            assert playground_page.ajax_data_page.check_label_is_present()
