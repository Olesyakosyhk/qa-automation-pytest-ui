from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.mixins import BlueButtonMixin
from resources.common_locators import CommonLocators


__all__ = [
    'ClassAttributePage',
]


class ClassAttributePage(BasePage, BlueButtonMixin):
    """
    Поиск основной кнопки, появляющейся рандомно среди других кнопок.

    Page URL:
        http://uitestingplayground.com/classattr
    """

    def accept_alert(self) -> None:
        alert = self.switch_to_alert()
        alert.accept()

    # Проверки...
    def check_presents_btn(self) -> WebElement | bool:
        selectors = [
            CommonLocators.BLUE_BTN,
            CommonLocators.YELLOW_BTN,
            CommonLocators.GREEN_BTN,
        ]
        return self.wait_for_all_elements_are_visible_by_selector(selector_array=selectors)

    def check_btn_is_clickable_elements(self) -> WebElement | bool:
        locators = [
            CommonLocators.BLUE_BTN,
            CommonLocators.YELLOW_BTN,
            CommonLocators.GREEN_BTN,
        ]
        return self.is_clickable_elements(locators_array=locators)
