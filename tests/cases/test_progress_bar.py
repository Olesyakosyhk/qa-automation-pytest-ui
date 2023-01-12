import allure

from pages import PlaygroundPage


class TestProgressBar:
    def test_progress_bar_positive(
            self,
            playground_page: PlaygroundPage,
    ):
        with allure.step('Переход на страницу "progress_bar"'):
            playground_page.main_page.go_to_page(name_page='progress_bar')

        with allure.step('Нажать на синюю кнопку "Start"'):
            playground_page.common_methods.click_blue_btn()

        with allure.step('Нажать на кнопку "Stop", когда прогресс достигнет 75%'):
            playground_page.progress_bar.click_stop_btn()

        with allure.step('Проверка, что прогресс более/равен 75%'):
            playground_page.progress_bar.check_result_progress_bar()
