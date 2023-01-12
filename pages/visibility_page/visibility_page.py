from pages.base import BaseUI
from resources.common_locators import CommonLocators


class VisibilityPage(BaseUI):
    """
    http://uitestingplayground.com/visibility
    """
    # Функции...
    def click_blue_btn(self) -> tuple:
        red_btn_element = self.find_and_wait_element(CommonLocators.RED_BTN)
        self.click_btn(CommonLocators.BLUE_BTN)
        return red_btn_element

    def check_is_elements_present(self) -> bool:
        locators = [
            CommonLocators.BLUE_BTN,
            CommonLocators.RED_BTN,
            CommonLocators.YELLOW_BTN,
            CommonLocators.GREEN_BTN,
        ]
        return self.wait_for_all_elements_are_visible_by_selector(locators)

    def check_visible_btn(self, element) -> bool:
        return self.find_staleness_of_element(element)

    def check_visible_blue_btn(self) -> bool:
        return self.find_and_wait_element(CommonLocators.BLUE_BTN)

    def check_visible_green_btn(self) -> bool:
        return self.find_and_wait_element(CommonLocators.GREEN_BTN)

    def check_visible_yellow_btn(self) -> bool:
        return self.find_and_wait_invisibility_element(CommonLocators.YELLOW_BTN)
