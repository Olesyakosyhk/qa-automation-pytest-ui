import allure

from pages import Pages


class TestScrollbarsPage:
    def test_scrollbars_page_positive(
            self,
            playground_page: Pages,
    ):
        with allure.step('Переход на страницу "scrollbars"'):
            playground_page.scrollbars_page.go_to_page()

        with allure.step('Поскроллить до необходимой синей кнопки'):
            playground_page.scrollbars_page.scroll_to_blue_btn()

        with allure.step('Нажать синюю кнопку'):
            playground_page.scrollbars_page.scroll_to_blue_btn()

    def test_scrollbars_page_no_scroll(
            self,
            playground_page: Pages,
    ):
        with allure.step('Переход на страницу "scrollbars"'):
            playground_page.scrollbars_page.go_to_page()

        with allure.step('Нажать синюю кнопку, без скролла'):
            playground_page.scrollbars_page.scroll_to_blue_btn()
