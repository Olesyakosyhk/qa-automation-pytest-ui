from selenium.webdriver.common.by import By

from app.components.common_button import BlueButton
from core_ui.components import Component
from core_ui.page import BasePage


__all__ = [
    'ClientSideDelayPage',
]


class ClientSideDelayPage(BasePage):
    """
    Учимся ждать появления элемента.
    Page URL:
        http://uitestingplayground.com/clientdelay
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)
        self.label = Component(
            driver=self.driver,
            locator_type=By.CSS_SELECTOR,
            locator_path='[class="bg-success"]',
        )

    def check_label_text_is_present(self) -> bool:
        if self.label.find_and_wait_element(timeout=15):
            return self.label.check_text(text='Data calculated on the client side.')
