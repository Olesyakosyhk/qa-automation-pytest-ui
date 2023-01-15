from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from resources.common_locators import CommonLocators


__all__ = [
    'DynamicIDPage',
]


class DynamicIDPage(BasePage):
    """
       Учимся ждать искать надежный атрибут.

       Page URL:
           http://uitestingplayground.com/dynamicid
       """

    def check_is_present_dynamic_id_btn(self) -> WebElement | bool:
        return self.is_element_present(CommonLocators.BLUE_BTN)

    def check_is_clickable_dynamic_id_btn(self) -> WebElement | bool:
        return self.is_clickable(CommonLocators.BLUE_BTN)
