import allure

from pages import PlaygroundPage


class TestNonBreakingSpace:
    def test_non_breaking_space_positive(
            self,
            playground_page: PlaygroundPage,
    ):
        with allure.step('Переход на страницу "non_breaking_space"'):
            playground_page.main_page.go_to_page(name_page='non_breaking_space')

        with allure.step('Проверка наличия кнопки "My Button" по xpath'):
            assert playground_page.non_breaking_space.check_btn_is_present()
