from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.mixins import BlueButtonMixin
from resources.common_locators import CommonLocators


__all__ = [
    'ClickPage',
]


class ClickPage(BasePage, BlueButtonMixin):
    """
    Запись нажатия кнопки.

    Page URL:
        http://uitestingplayground.com/click
    """

    # Функции...
    def click_blue_btn(self) -> None:
        self.click_btn(CommonLocators.BLUE_BTN)

    def check_green_btn_is_present(self) -> WebElement | bool:
        return self.find_and_wait_element(CommonLocators.GREEN_BTN)
