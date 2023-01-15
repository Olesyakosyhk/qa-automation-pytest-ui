import allure

from pages import Pages


class TestProgressBarPage:
    def test_progress_bar_positive(
            self,
            playground_page: Pages,
    ):
        with allure.step('Переход на страницу "progress_bar"'):
            playground_page.progress_bar_page.go_to_page()

        with allure.step('Нажать на синюю кнопку "Start"'):
            playground_page.progress_bar_page.click_blue_btn()

        with allure.step('Нажать на кнопку "Stop", когда прогресс достигнет 75%'):
            playground_page.progress_bar_page.click_stop_btn()

        with allure.step('Проверка, что прогресс более/равен 75%'):
            playground_page.progress_bar_page.check_result_progress_bar()
