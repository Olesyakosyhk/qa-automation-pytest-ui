from pages.base import BaseUI
from resources.common_locators import CommonLocators


class CommonMethods(BaseUI):

    # Нажатие синей кнопки...
    def click_blue_btn(self) -> None:
        self.click_btn(CommonLocators.BLUE_BTN)
