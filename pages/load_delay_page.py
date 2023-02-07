from components.common_button import BlueButton
from components.button import Button
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)
