import allure
import pytest

from pages import Pages


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
    ):
        with allure.step('Переход на страницу "mouse_over"'):
            playground_page.mouse_over_page.go_to_page()

        with allure.step('Клик по ссылке'):
            playground_page.mouse_over_page.click_link_for_page()

        with allure.step('2й клик по ссылке'):
            playground_page.mouse_over_page.click_modified_link()

        with allure.step('Проверка количества нажатий на ссылку'):
            assert playground_page.mouse_over_page.check_the_link_clicked_times()
