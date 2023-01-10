from selenium.webdriver.common.by import By

from core.settings import BASE_URL
from pages.base import BaseUI


class ClassAttribute(BaseUI):

    CLASS_ATTRIBUTE_URL = f'{BASE_URL}/classattr'

    # Локаторы...
    BLUE_BTN = (By.CSS_SELECTOR, '[class*="btn-primary"]')
    YELLOW_BTN = (By.CSS_SELECTOR, '[class*="btn-warning"]')
    GREEN_BTN = (By.CSS_SELECTOR, '[class*="btn-success"]')

    # Функции...
    def click_blue_btn(self) -> None:
        btn = self.find_and_wait_elements(self.BLUE_BTN)[0]
        btn.click()

    def accept_alert(self):
        alert = self.switch_to_alert()
        alert.accept()

    # Проверки...
    def check_class_attribute_url(self) -> bool:
        return self.get_current_url() == self.CLASS_ATTRIBUTE_URL

    def check_presents_btn(self) -> bool:
        selectors = [
            self.BLUE_BTN,
            self.YELLOW_BTN,
            self.GREEN_BTN,
        ]
        return self.wait_for_all_elements_are_visible_by_selector(selector_array=selectors)

    def check_btn_is_clickable_elements(self):
        locators = [
            self.BLUE_BTN,
            self.YELLOW_BTN,
            self.GREEN_BTN,
        ]
        return self.is_clickable_elements(locators_array=locators)
