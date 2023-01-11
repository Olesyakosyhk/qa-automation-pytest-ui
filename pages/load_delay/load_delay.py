from selenium.webdriver.common.by import By

from core.settings import BASE_URL
from pages.base import BaseUI
from resources.common_locators import CommonLocators


class LoadDelay(BaseUI):
    """
    http://uitestingplayground.com/loaddelay
    """

    LOAD_DELAY_URL = f'{BASE_URL}/loaddelay'

    #  Функции...
    def check_load_delay_url(self) -> bool:
        return self.get_current_url() == self.LOAD_DELAY_URL
    
    def check_btn_is_present(self) -> bool:
        return self.is_clickable(CommonLocators.BLUE_BTN)
