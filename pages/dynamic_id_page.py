from selenium.webdriver.remote.webelement import WebElement

from components.common_button import BlueButton
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)
