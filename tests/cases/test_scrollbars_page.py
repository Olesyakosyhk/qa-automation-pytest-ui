import allure
import pytest

from pages import Pages


@allure.parent_suite('REGRESSION')
@allure.suite('ScrollbarsPage')
@pytest.mark.regression
@pytest.mark.scrollbars_page
class TestScrollbarsPage:

    @allure.title('Тест №9 для страницы "scrollbars".')
    @allure.description('Скролл до кнопки и последующее её нажатие.')
    def test_scrollbars_page_positive(
            self,
            playground_page: Pages,
    ):
        with allure.step('Переход на страницу "scrollbars"'):
            playground_page.scrollbars_page.scrollbars_page_url.go_to_page()

        with allure.step('Поскроллить до необходимой синей кнопки'):
            playground_page.scrollbars_page.blue_button.scroll()

        with allure.step('Нажать синюю кнопку'):
            playground_page.scrollbars_page.blue_button.click()

    @allure.title('Тест №9.2 для страницы "scrollbars".')
    @allure.description('Нажатие синей кнопки без скролла.')
    def test_scrollbars_page_no_scroll(
            self,
            playground_page: Pages,
    ):
        with allure.step('Переход на страницу "scrollbars".'):
            playground_page.scrollbars_page.scrollbars_page_url.go_to_page()

        with allure.step('Нажать синюю кнопку без скролла.'):
            playground_page.scrollbars_page.blue_button.click()
