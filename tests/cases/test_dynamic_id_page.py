import allure
import pytest

from app.pages import Pages


@allure.parent_suite('REGRESSION')
@allure.suite('TestDynamicID')
@pytest.mark.regression
@pytest.mark.dynamic_id_page
class TestDynamicIDPage:

    @allure.title('Тест №10 для страницы "dynamic_id".')
    @allure.description(
        'Тест, чтобы убедиться, что  динамический идентификатор не используется для идентификации кнопки.',
    )
    def test_dynamic_id_page_positive(
            self,
            playground_page: Pages,
    ) -> None:
        with allure.step('Переход на страницу "dynamic_id"'):
            playground_page.dynamic_id_page.go_to_page_by_url()

        with allure.step('Проверка на наличие кнопки на странице.'):
            assert playground_page.dynamic_id_page.blue_button.element

        with allure.step('Проверка на активность кнопки.'):
            assert playground_page.dynamic_id_page.blue_button.is_clickable()
