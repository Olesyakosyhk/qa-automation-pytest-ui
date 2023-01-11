from selenium.webdriver.common.by import By

from pages.base import BaseUI
from resources.common_locators import CommonLocators


class TextInput(BaseUI):
    """
    http://uitestingplayground.com/textinput
    """

    # Локаторы...
    INPUT_NAME = (By.ID, 'newButtonName')
    CUSTOM_NAME_BTN = "Button That Should Change it's Name Based on Input Value"

    def input_name_for_btn(self, new_name: str) -> None:
        new_btn_name = self.find_and_wait_element(self.INPUT_NAME)
        new_btn_name.send_keys(new_name)

    def click_blue_btn(self):
        self.click_btn(CommonLocators.BLUE_BTN)

    def check_name_blue_btn(self) -> bool:
        return self.find_and_wait_element(CommonLocators.BLUE_BTN).text == self.CUSTOM_NAME_BTN

    def check_new_name_blue_btn(self, new_name) -> bool:
        return self.find_and_wait_element(CommonLocators.BLUE_BTN).text == new_name
