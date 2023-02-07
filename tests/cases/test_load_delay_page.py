import allure
import pytest

from pages import Pages


@allure.parent_suite('REGRESSION')
@allure.suite('LoadDelayPage')
@pytest.mark.regression
@pytest.mark.load_delay_page
class TestLoadDelayPage:

    @allure.title('Тест №4 для страницы "load_delay".')
    @allure.description('Проверка наличия кликабельной кнопки на странице.')
    def test_load_delay_positive(
            self,
            playground_page: Pages,
            go_to_main_page,
    ):
        with allure.step('Переход на страницу "load_delay"'):
            playground_page.main_page.click_load_delay_btn()

        with allure.step('Проверка наличия кликабельной кнопки на странице "load_delay"'):
            assert playground_page.load_delay_page.blue_button.find_and_wait_element()

    @allure.title('Тест №4.2 для страницы "load_delay".')
    @allure.description('Проверка url на странице "load_delay".')
    def test_load_delay_url(
            self,
            playground_page: Pages,
            go_to_main_page,
    ):
        with allure.step('Переход на страницу "load_delay"'):
            playground_page.load_delay_page.go_to_page()

        with allure.step('Проверка url на странице "load_delay"'):
            assert playground_page.load_delay_page.check_url()
