from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from resources.common_locators import CommonLocators


__all__ = [
    'VisibilityPage',
]


class VisibilityPage(BasePage):
    """
    Проверяем видимость элемента на экране.

     Page URL:
        http://uitestingplayground.com/visibility
    """
    def click_blue_btn(self) -> tuple:
        red_btn_element = self.find_and_wait_element(CommonLocators.RED_BTN)
        self.click_btn(CommonLocators.BLUE_BTN)
        return red_btn_element

    def check_is_elements_present(self) -> WebElement | bool:
        locators = [
            CommonLocators.BLUE_BTN,
            CommonLocators.RED_BTN,
            CommonLocators.YELLOW_BTN,
            CommonLocators.GREEN_BTN,
        ]
        return self.wait_for_all_elements_are_visible_by_selector(locators)

    def check_visible_btn(self, element) -> WebElement | bool:
        return self.find_staleness_of_element(element)

    def check_visible_blue_btn(self) -> WebElement | bool:
        return self.find_and_wait_element(CommonLocators.BLUE_BTN)

    def check_visible_green_btn(self) -> WebElement | bool:
        return self.find_and_wait_element(CommonLocators.GREEN_BTN)

    def check_visible_yellow_btn(self) -> WebElement | bool:
        return self.find_and_wait_invisibility_element(CommonLocators.YELLOW_BTN)
