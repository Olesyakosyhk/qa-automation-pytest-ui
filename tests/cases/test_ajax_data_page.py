import allure
import pytest

from app.pages import Pages


@allure.parent_suite('REGRESSION')
@allure.suite('AJAXDataPage')
@pytest.mark.regression
@pytest.mark.ajax_data_page
class TestAJAXDataPage:

    @allure.title('Тест №5 для страницы "ajax_data".')
    @allure.description('Ждем ответа при AJAX запросе. Проверка лейбла на странице AJAXData')
    def test_ajax_data_positive(
            self,
            playground_page: Pages,
            go_to_main_page: None,
    ) -> None:
        with allure.step('Переход на страницу "ajax"'):
            playground_page.ajax_data_page.go_to_page_by_url()

        with allure.step('Проверка url страницы "ajax"'):
            assert playground_page.ajax_data_page.check_url()

        with allure.step('Нажать на синюю кнопку'):
            playground_page.ajax_data_page.blue_button.click()

        with allure.step('Проверка лейбла'):
            assert playground_page.ajax_data_page.check_label_is_present()
