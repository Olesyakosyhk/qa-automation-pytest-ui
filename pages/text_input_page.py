from selenium.webdriver.common.by import By

from components.common_button import BlueButton
from pages.base_page import BasePage
from resources.common_locators import CommonLocators


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

    # Локаторы...
    INPUT_NAME = (By.ID, 'newButtonName')
    CUSTOM_NAME_BTN = "Button That Should Change it's Name Based on Input Value"

    def input_name_for_btn(self, new_name: str) -> None:
        new_btn_name = self.find_and_wait_element(self.INPUT_NAME)
        new_btn_name.send_keys(new_name)

    def click_blue_btn(self) -> None:
        self.click_btn(CommonLocators.BLUE_BTN)

    def check_name_blue_btn(self) -> bool:
        return self.find_and_wait_element(CommonLocators.BLUE_BTN).text == self.CUSTOM_NAME_BTN

    def check_new_name_blue_btn(self, new_name: str) -> bool:
        return self.find_and_wait_element(CommonLocators.BLUE_BTN).text == new_name
