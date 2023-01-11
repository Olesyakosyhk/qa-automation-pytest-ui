from selenium.webdriver.common.by import By

from core.settings import BASE_URL
from pages.base import BaseUI
from resources.common_locators import CommonLocators


class ClassAttribute(BaseUI):
    """
    http://uitestingplayground.com/classattr
    """

    CLASS_ATTRIBUTE_URL = f'{BASE_URL}/classattr'

    # Функции...
    def accept_alert(self):
        alert = self.switch_to_alert()
        alert.accept()

    # Проверки...
    def check_class_attribute_url(self) -> bool:
        return self.get_current_url() == self.CLASS_ATTRIBUTE_URL

    def check_presents_btn(self) -> bool:
        selectors = [
            CommonLocators.BLUE_BTN,
            CommonLocators.YELLOW_BTN,
            CommonLocators.GREEN_BTN,
        ]
        return self.wait_for_all_elements_are_visible_by_selector(selector_array=selectors)

    def check_btn_is_clickable_elements(self):
        locators = [
            CommonLocators.BLUE_BTN,
            CommonLocators.YELLOW_BTN,
            CommonLocators.GREEN_BTN,
        ]
        return self.is_clickable_elements(locators_array=locators)
