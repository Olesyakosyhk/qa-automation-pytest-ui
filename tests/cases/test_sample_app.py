import allure
from faker import Faker

from pages import PlaygroundPage


class TestSampleApp:
    def test_sample_app_positive(
            self,
            playground_page: PlaygroundPage,
            fake: Faker,
    ):
        with allure.step('Переход на страницу "sample_app"'):
            playground_page.main_page.go_to_page(name_page='sample_app')

        with allure.step('Авторизация пользователя '):
            name = str(fake.first_name())
            playground_page.sample_app.do_login_via_log_pass(login=name, password='pwd')

        with allure.step(f'Проверка успешной авторизации пользователя {name}'):
            assert playground_page.sample_app.check_login_status(name=name)
