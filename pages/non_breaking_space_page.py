from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


__all__ = [
    'NonBreakingSpacePage',
]


class NonBreakingSpacePage(BasePage):
    """
    Поиск элемента с неразрывным пробелом.

    Page URL:
        http://uitestingplayground.com/nbsp
    """

    # Локаторы...
    MY_BTN = (By.XPATH, '//button[contains(text(), "My Button")]')

    def check_btn_is_present(self) -> WebElement | bool:
        return self.find_and_wait_element(self.MY_BTN)
