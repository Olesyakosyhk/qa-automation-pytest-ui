import allure

from pages import Pages


class TestMouseOverPage:
    def test_mouse_over_page_positive(
            self,
            playground_page: Pages,
    ):
        with allure.step('Переход на страницу "mouse_over"'):
            playground_page.mouse_over_page.go_to_page()

        with allure.step('Клик по ссылке'):
            playground_page.mouse_over_page.click_link_for_page()

        with allure.step('2й клик по ссылке'):
            playground_page.mouse_over_page.click_modified_link()

        with allure.step('Проверка количества нажатий на ссылку'):
            assert playground_page.mouse_over_page.check_the_link_clicked_times()
