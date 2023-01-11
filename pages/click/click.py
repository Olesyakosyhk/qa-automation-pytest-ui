from core.settings import BASE_URL
from pages.base import BaseUI
from resources.common_locators import CommonLocators


class ClickPage(BaseUI):
    """
    http://uitestingplayground.com/click
    """
    CLICK_PAGE_URL = f'{BASE_URL}/click'

    # Функции...
    def click_blue_btn(self) -> None:
        self.click_btn(CommonLocators.BLUE_BTN)

    def check_green_btn_is_present(self) -> bool:
        return self.find_and_wait_element(CommonLocators.GREEN_BTN)
