from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from resources.common_locators import CommonLocators


__all__ = [
    'LoadDelayPage',
]


class LoadDelayPage(BasePage):
    """
    Тест может ожидать загрузки страницы.

    Page URL:
        http://uitestingplayground.com/loaddelay
    """

    def check_btn_is_present(self) -> WebElement | bool:
        return self.is_clickable(CommonLocators.BLUE_BTN)
