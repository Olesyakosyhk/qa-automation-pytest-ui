import allure

from pages import Pages


class TestNonBreakingSpacePage:
    def test_non_breaking_space_positive(
            self,
            playground_page: Pages,
    ):
        with allure.step('Переход на страницу "non_breaking_space"'):
            playground_page.non_breaking_space_page.go_to_page()

        with allure.step('Проверка наличия кнопки "My Button" по xpath'):
            assert playground_page.non_breaking_space_page.check_btn_is_present()
