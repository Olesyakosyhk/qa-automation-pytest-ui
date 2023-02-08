import allure
import pytest

from app.pages import Pages


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
    ) -> None:
        with allure.step('Переход на страницу "scrollbars"'):
            playground_page.scrollbars_page.go_to_page_by_url()

        with allure.step('Поскроллить до необходимой синей кнопки'):
            playground_page.scrollbars_page.scroll_to_blue_btn()

        with allure.step('Нажать синюю кнопку'):
            playground_page.scrollbars_page.blue_button.click()

    @allure.title('Тест №9.2 для страницы "scrollbars".')
    @allure.description('Нажатие синей кнопки без скролла.')
    def test_scrollbars_page_no_scroll(
            self,
            playground_page: Pages,
    ) -> None:
        with allure.step('Переход на страницу "scrollbars".'):
            playground_page.scrollbars_page.go_to_page_by_url()

        with allure.step('Нажать синюю кнопку без скролла.'):
            playground_page.scrollbars_page.blue_button.click()
