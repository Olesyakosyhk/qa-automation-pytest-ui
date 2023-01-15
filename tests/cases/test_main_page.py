import allure

from pages import Pages


class TestMainPage:

    def test_main_page_positive(
            self,
            playground_page: Pages,
    ):
        with allure.step('Переход на страницу площадки для UI Test'):
            playground_page.main_page.go_to_page()

        with allure.step('Проверка наличия всех разделов платформы'):
            assert playground_page.main_page.check_for_all_elements_are_visible_by_selector()

        with allure.step('Проверка активности всех разделов платформы'):
            assert playground_page.main_page.check_element_is_clickable()
