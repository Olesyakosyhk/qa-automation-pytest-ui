from selenium.webdriver.common.by import By

from components.common_button import BlueButton
from components.page_url import PageURL
from pages.base_page import BasePage


__all__ = [
    'SampleAppPage',
]


class SampleAppPage(BasePage):
    """
    Учимся работать с динамически генерируемыми атрибутами элементов.

     Page URL:
        http://uitestingplayground.com/sampleapp
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)

        self.sample_app_page_url = PageURL(
            driver=self.driver,
            path='/sampleapp',
        )

    # Локаторы...
    LOGIN_INPUT = (By.NAME, 'UserName')
    PASSWORD_INPUT = (By.NAME, 'Password')
    LOGIN_STATUS = (By.ID, 'loginstatus')

    def _auth_by(
            self,
            login: str,
            password: str,
    ) -> None:
        _login = self.find_and_wait_element(self.LOGIN_INPUT)
        _login.send_keys(login)
        self.find_and_wait_element(self.PASSWORD_INPUT).send_keys(password)

    def do_login_via_log_pass(self, login: str, password: str) -> None:
        self._auth_by(login=login, password=password)

    def check_login_status(self, name: str) -> bool:
        return self.find_and_wait_element(self.LOGIN_STATUS).text == f'Welcome, {name}!'
