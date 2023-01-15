import allure

from pages import Pages


class TestClickPage:
    def test_click_page_positive(
            self,
            playground_page: Pages,
    ):
        with allure.step('Переход на страницу "click_page"'):
            playground_page.click_page.go_to_page()

        with allure.step('Нажать на синюю кнопку'):
            playground_page.click_page.click_blue_btn()

        with allure.step('Поверка изменения цвета синей кнопки на зеленый'):
            assert playground_page.click_page.check_green_btn_is_present()
