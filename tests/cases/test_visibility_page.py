import allure
import pytest

from app.pages import Pages


@allure.parent_suite('REGRESSION')
@allure.suite('VisibilityPage')
@pytest.mark.regression
@pytest.mark.main_page
class TestVisibilityPage:

    @allure.title('Тест №13 для страницы "visibility".')
    @allure.description('Проверка видимости всех кнопок на странице.')
    def test_visibility_page_positive(
            self,
            playground_page: Pages,
    ):
        with allure.step('Переход на страницу "visibility"'):
            playground_page.visibility_page.go_to_page_by_url()

        with allure.step('Проверка видимости всех кнопок: синяя, желтая, красная, зеленая'):
            assert playground_page.visibility_page.check_is_elements_present()

        with allure.step('Нажать на синюю кнопку'):
            playground_page.visibility_page.blue_button.click()

        with allure.step('Проверка видимости синей кнопки'):
            assert playground_page.visibility_page.blue_button.find_and_wait_element()

        with allure.step('Проверка отсутствия красной кнопки'):
            assert playground_page.visibility_page.red_button.find_staleness_of_element()

        with allure.step('Проверка видимости зеленой кнопки'):
            assert playground_page.visibility_page.green_button.find_and_wait_element()

        with allure.step('Проверка не видимости желтой кнопки'):
            assert playground_page.visibility_page.yellow_button.find_and_wait_invisibility_element()
