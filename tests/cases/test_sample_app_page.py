import allure
from faker import Faker

from pages import Pages


class TestSampleAppPage:
    def test_sample_app_positive(
            self,
            playground_page: Pages,
            fake: Faker,
    ):
        with allure.step('Переход на страницу "sample_app"'):
            playground_page.sample_app_page.go_to_page()

        with allure.step('Авторизация пользователя '):
            name = str(fake.first_name())
            playground_page.sample_app_page.do_login_via_log_pass(login=name, password='pwd')

        with allure.step(f'Проверка успешной авторизации пользователя {name}'):
            assert playground_page.sample_app_page.check_login_status(name=name)
