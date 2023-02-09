from selenium.webdriver.common.by import By

from app.components.common_button import BlueButton
from core_ui.components import Input
from core_ui.page import BasePage


__all__ = [
    'TextInputPage',
]


class TextInputPage(BasePage):
    """
    Учимся вводить текст в поле ввода.

    Page URL:
        http://uitestingplayground.com/textinput
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)

        self.input_name = Input(
            driver=self.driver,
            locator_type=By.ID,
            locator_path='newButtonName',
        )
