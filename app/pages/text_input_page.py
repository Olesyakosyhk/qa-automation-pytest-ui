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
    DEFAULT_TEXT_BTN = "Button That Should Change it's Name Based on Input Value"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)

        self.input_name = Input(
            driver=self.driver,
            locator_type=By.ID,
            locator_path='newButtonName',
        )

    def check_default_text_blue_btn(self) -> bool:
        return self.blue_button.check_text(text=self.DEFAULT_TEXT_BTN)
