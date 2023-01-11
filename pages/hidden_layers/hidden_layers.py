from selenium.webdriver.common.by import By

from pages.base import BaseUI


class HiddenLayers(BaseUI):
    """
    http://uitestingplayground.com/hiddenlayers
    """

    # Локаторы...
    GREEN_BTN = (By.ID, 'greenButton')
    BLUE_BTN = (By.ID, 'blueButton')

    # Функции...
    def click_green_btn(self) -> None:
        self.click_btn(self.GREEN_BTN)

    def check_blue_btn_is_present(self) -> bool:
        return self.find_and_wait_element(self.BLUE_BTN)
