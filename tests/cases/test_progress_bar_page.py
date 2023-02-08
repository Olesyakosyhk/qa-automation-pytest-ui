import allure
import pytest

from app.pages import Pages


@allure.parent_suite('REGRESSION')
@allure.suite('ProgressBarPage')
@pytest.mark.regression
@pytest.mark.progress_bar_page
class TestProgressBarPage:

    @allure.title('Тест №12 для страницы "progress_bar".')
    @allure.description('Проверка, что прогресс более/равен 75%.')
    def test_progress_bar_positive(
            self,
            playground_page: Pages,
    ) -> None:
        with allure.step('Переход на страницу "progress_bar"'):
            playground_page.progress_bar_page.go_to_page_by_url()

        with allure.step('Нажать на синюю кнопку "Start"'):
            playground_page.progress_bar_page.blue_button.click()

        with allure.step('Нажать на кнопку "Stop", когда прогресс достигнет 75%'):
            playground_page.progress_bar_page.stop_button.click()

        with allure.step('Проверка, что прогресс более/равен 75%'):
            playground_page.progress_bar_page.check_result_progress_bar()
