import allure

from pages import PlaygroundPage


class TestScrollbarsPage:
    def test_scrollbars_page_positive(
            self,
            playground_page: PlaygroundPage,
    ):
        with allure.step('Переход на страницу "scrollbars"'):
            playground_page.main_page.go_to_page(name_page='scrollbars')

        with allure.step('Поскроллить до необходимой синей кнопки'):
            playground_page.scrollbars.scroll_to_blue_btn()

        with allure.step('Нажать синюю кнопку'):
            playground_page.scrollbars.scroll_to_blue_btn()

    def test_scrollbars_page_no_scroll(
            self,
            playground_page: PlaygroundPage,
    ):
        with allure.step('Переход на страницу "scrollbars"'):
            playground_page.main_page.go_to_page(name_page='scrollbars')

        with allure.step('Нажать синюю кнопку, без скролла'):
            playground_page.scrollbars.scroll_to_blue_btn()
