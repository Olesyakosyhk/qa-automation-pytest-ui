import allure
import pytest

from app.pages import Pages


@allure.parent_suite('REGRESSION')
@allure.suite('NonBreakingSpacePage')
@pytest.mark.regression
@pytest.mark.non_breaking_space_page
class TestNonBreakingSpacePage:

    @allure.title('Тест №16 для страницы "non_breaking_space".')
    @allure.description('Проверка наличия кнопки "My Button" по xpath.')
    def test_non_breaking_space_positive(
            self,
            playground_page: Pages,
    ) -> None:
        with allure.step('Переход на страницу "non_breaking_space"'):
            playground_page.non_breaking_space_page.go_to_page_by_url()

        with allure.step('Проверка наличия кнопки "My Button" по xpath'):
            assert playground_page.non_breaking_space_page.my_button.element
