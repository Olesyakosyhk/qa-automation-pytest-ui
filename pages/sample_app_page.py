from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from resources.common_locators import CommonLocators


__all__ = [
    'SampleAppPage',
]


class SampleAppPage(BasePage):
    """
    Учимся работать с динамически генерируемыми атрибутами элементов.

     Page URL:
        http://uitestingplayground.com/sampleapp
    """

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
        self.click_btn(CommonLocators.BLUE_BTN)

    def do_login_via_log_pass(self, login: str, password: str) -> None:
        self._auth_by(login=login, password=password)

    def check_login_status(self, name: str) -> bool:
        return self.find_and_wait_element(self.LOGIN_STATUS).text == f'Welcome, {name}!'