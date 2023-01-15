import allure

from pages import Pages


class TestVisibilityPage:
    def test_visibility_page_positive(
            self,
            playground_page: Pages,
    ):
        with allure.step('Переход на страницу "visibility"'):
            playground_page.visibility_page.go_to_page()

        with allure.step('Проверка видимости всех кнопок: синяя, желтая, красная, зеленая'):
            assert playground_page.visibility_page.check_is_elements_present()

        with allure.step('Нажать на синюю кнопку'):
            red_btn = playground_page.visibility_page.click_blue_btn()

        with allure.step('Проверка видимости синей кнопки'):
            assert playground_page.visibility_page.check_visible_blue_btn()

        with allure.step('Проверка отсутствия красной кнопки'):
            assert playground_page.visibility_page.check_visible_btn(element=red_btn)

        with allure.step('Проверка видимости зеленой кнопки'):
            assert playground_page.visibility_page.check_visible_green_btn()

        with allure.step('Проверка не видимости желтой кнопки'):
            assert playground_page.visibility_page.check_visible_yellow_btn()