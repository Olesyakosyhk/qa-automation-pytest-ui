import allure
import pytest

from app.pages import Pages


@allure.parent_suite('REGRESSION')
@allure.suite('HiddenLayersPage')
@pytest.mark.regression
@pytest.mark.hidden_layers_page
class TestHiddenLayersPage:

    @allure.title('Тест №3 для страницы "hidden_layers_page".')
    @allure.description('Проверка: нельзя нажать зеленую кнопку 2ды.')
    def test_hidden_layers_positive(
            self,
            playground_page: Pages,
            go_to_hidden_layers_page,
    ):
        with allure.step('Нажать на зеленую кнопку'):
            playground_page.hidden_layers_page.green_button.click()

        with pytest.raises(Exception) as exc_info:
            with allure.step('Повторить нажатие на зеленую кнопку'):
                playground_page.hidden_layers_page.green_button.click()

        with allure.step(f'Проверка ответа | {exc_info.value.args[0]=}'):
            assert exc_info.value.args[0].startswith('element click intercepted:')
