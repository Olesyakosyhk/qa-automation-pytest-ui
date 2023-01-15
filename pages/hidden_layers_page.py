from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from resources.common_locators import CommonLocators


__all__ = [
    'HiddenLayersPage',
]


class HiddenLayersPage(BasePage):
    """
    Тест не взаимодействует с элементами, невидимыми из-за z-порядка.

    Page URL:
        http://uitestingplayground.com/hiddenlayers
    """

    def click_green_btn(self) -> None:
        self.click_btn(CommonLocators.GREEN_BTN)

    def check_blue_btn_is_present(self) -> WebElement | bool:
        return self.find_and_wait_element(CommonLocators.BLUE_BTN)
