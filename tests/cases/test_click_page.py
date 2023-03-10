import allure
import pytest

from app.pages import Pages


@allure.parent_suite('REGRESSION')
@allure.suite('ClickPage')
@pytest.mark.regression
@pytest.mark.click_page
class TestClickPage:

    @allure.title('Тест №7 для страницы "click".')
    @allure.description('Поверка изменения цвета синей кнопки на зеленый')
    def test_click_page_positive(
            self,
            playground_page: Pages,
    ) -> None:
        with allure.step('Переход на страницу "click_page"'):
            playground_page.click_page.go_to_page_by_url()

        with allure.step('Нажать на синюю кнопку'):
            playground_page.click_page.blue_button.click()

        with allure.step('Поверка изменения цвета синей кнопки на зеленый'):
            assert playground_page.click_page.green_button.element
