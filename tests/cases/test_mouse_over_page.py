import allure
import pytest

from app.pages import Pages


@allure.parent_suite('REGRESSION')
@allure.suite('MouseOverPage')
@pytest.mark.regression
@pytest.mark.mouse_over_page
class TestMouseOverPage:

    @allure.title('Тест №15 для страницы "mouse_over".')
    @allure.description('Проверка количества нажатий на ссылку.')
    def test_mouse_over_page_positive(
            self,
            playground_page: Pages,
    ) -> None:
        with allure.step('Переход на страницу "mouse_over"'):
            playground_page.mouse_over_page.go_to_page_by_url()

        with allure.step('Навести курсор мыши на кнопку'):
            playground_page.mouse_over_page.original_element_btn.mouseover()

        with allure.step('2 клика по ссылке'):
            playground_page.mouse_over_page.modified_element_button.click(count=2)

        with allure.step('Проверка количества нажатий на ссылку'):
            assert playground_page.mouse_over_page.counter.check_text('2')
