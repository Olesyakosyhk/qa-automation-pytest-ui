from selenium.webdriver.common.by import By

from pages.base import BaseUI


class NonBreakingSpace(BaseUI):
    """
    http://uitestingplayground.com/nbsp
    """

    # Локаторы...
    MY_BTN = (By.XPATH, '//button[contains(text(), "My Button")]')

    # Функции...
    def check_btn_is_present(self) -> bool:
        return self.find_and_wait_element(self.MY_BTN)
