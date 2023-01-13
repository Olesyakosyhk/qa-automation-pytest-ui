import allure

from pages import PlaygroundPage


class TestMouseOverPage:
    def test_mouse_over_page_positive(
            self,
            playground_page: PlaygroundPage,
    ):
        with allure.step('Переход на страницу "mouse_over"'):
            playground_page.main_page.go_to_page(name_page='mouse_over')

        with allure.step('Клик по ссылке'):
            playground_page.mouse_over.click_link_for_page()

        with allure.step('2й клик по ссылке'):
            playground_page.mouse_over.click_modified_link()

        with allure.step('Проверка количества нажатий на ссылку'):
            assert playground_page.mouse_over.check_the_link_clicked_times()
