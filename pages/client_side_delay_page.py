from selenium.webdriver.common.by import By

from components.common_button import BlueButton
from components.component import Component
from components.page_url import PageURL
from pages.base_page import BasePage


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

        self.client_side_delay_url = PageURL(
            driver=self.driver,
            path='/clientdelay',
        )

    def check_label_text_is_present(self) -> bool:
        if self.label.find_and_wait_element(timeout=15):
            return self.label.check_text(text='Data calculated on the client side.')
