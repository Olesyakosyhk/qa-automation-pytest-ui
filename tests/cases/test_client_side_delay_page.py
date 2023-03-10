import allure
import pytest

from app.pages import Pages


@allure.parent_suite('REGRESSION')
@allure.suite('ClientSideDelayPage')
@pytest.mark.regression
@pytest.mark.client_side_delay_page
class TestClientSideDelayPage:

    @allure.title('Тест №6 для страницы "client_side_delay".')
    @allure.description('Проверка ожидания появления текста метки')
    def test_client_side_delay_positive(
            self,
            playground_page: Pages,
    ) -> None:
        with allure.step('Переход на страницу "client_side_delay"'):
            playground_page.client_side_delay_page.go_to_page_by_url()

        with allure.step('Нажатие на кнопку'):
            playground_page.client_side_delay_page.blue_button.click()

        with allure.step('Проверка ожидания появления текста метки'):
            assert playground_page.client_side_delay_page.label.check_text(text='Data calculated on the client side.')
