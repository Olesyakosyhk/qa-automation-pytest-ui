from selenium.webdriver.common.by import By

from pages.base import BaseUI
from resources.common_locators import CommonLocators


class HiddenLayers(BaseUI):
    """
    http://uitestingplayground.com/hiddenlayers
    """

    # Функции...
    def click_green_btn(self) -> None:
        self.click_btn(CommonLocators.GREEN_BTN)

    def check_blue_btn_is_present(self) -> bool:
        return self.find_and_wait_element(CommonLocators.BLUE_BTN)
