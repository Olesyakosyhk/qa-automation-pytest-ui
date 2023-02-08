import allure
import pytest

from app.pages import Pages


@allure.parent_suite('REGRESSION')
@allure.suite('TestDynamicTable')
@pytest.mark.regression
@pytest.mark.dynamic_table_page
class TestDynamicTablePage:

    @allure.title('Тест №10 для страницы "dynamic_table".')
    @allure.description(
        'Получение для процесса Chrome значение загрузки процессора и сравнение его со значением на лэйбле',
    )
    def test_dynamic_table_page_positive(
            self,
            playground_page: Pages,
    ) -> None:
        with allure.step('Переход на страницу "dynamic_table"'):
            playground_page.dynamic_table_page.go_to_page_by_url()

        with allure.step('Получение для процесса Chrome значение загрузки процессора'):
            value_table_cpu = playground_page.dynamic_table_page.get_locator_chrome_cpu()

        with allure.step('Проверка на сравнение полученных данных cpu со значением на лэйбле.'):
            assert playground_page.dynamic_table_page.check_value_chrome_cpu(
                value_table_cpu=value_table_cpu,
            )
