from selenium.webdriver.common.by import By

from pages.base_page import BasePage


__all__ = [
    'ClientSideDelayPage',
]

from pages.mixins import BlueButtonMixin


class ClientSideDelayPage(BasePage, BlueButtonMixin):
    """
    Учимся ждать появления элемента.
    Page URL:
        http://uitestingplayground.com/clientdelay
    """

    # Локаторы...
    LABEL = (By.CSS_SELECTOR, '[class="bg-success"]')

    def check_label_text_is_present(self) -> bool:
        if self.find_and_wait_element(self.LABEL, 15):
            return self.find_and_wait_element(self.LABEL).text == 'Data calculated on the client side.'
