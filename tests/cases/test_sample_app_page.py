import allure
import pytest
from faker import Faker

from pages import Pages


@allure.parent_suite('REGRESSION')
@allure.suite('SampleAppPage')
@pytest.mark.regression
@pytest.mark.sample_app_page
class TestSampleAppPage:

    @allure.title('Тест №14 для страницы "sample_app".')
    @allure.description('Проверка успешной авторизации пользователя.')
    def test_sample_app_positive(
            self,
            playground_page: Pages,
            fake: Faker,
    ):
        with allure.step('Переход на страницу "sample_app".'):
            playground_page.sample_app_page.sample_app_page_url.go_to_page()

        with allure.step('Авторизация пользователя.'):
            name = str(fake.first_name())
            playground_page.sample_app_page.do_login_via_log_pass(login=name, password='pwd')
            playground_page.sample_app_page.blue_button.click()

        with allure.step(f'Проверка успешной авторизации пользователя {name}.'):
            assert playground_page.sample_app_page.check_login_status(name=name)
