from selenium.webdriver.common.by import By

from app.components.common_button import BlueButton
from core_ui.components import Input, Label
from core_ui.page import BasePage


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
        self.login_input = Input(
            driver=self.driver,
            locator_type=By.NAME,
            locator_path='UserName',
        )
        self.password_input = Input(
            driver=self.driver,
            locator_type=By.NAME,
            locator_path='Password',
        )
        self.label = Label(
            driver=self.driver,
            locator_type=By.ID,
            locator_path='loginstatus',
        )

    def _auth_by(
            self,
            login: str,
            password: str,
    ) -> None:
        self.login_input.set_text(login)
        self.password_input.set_text(password)

    def do_login_via_log_pass(
            self,
            login: str,
            password: str,
    ) -> None:
        self._auth_by(login=login, password=password)

    def check_login_status(self, name: str) -> bool:
        return self.label.check_text(f'Welcome, {name}!')
