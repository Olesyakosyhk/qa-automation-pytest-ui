from selenium.webdriver.common.by import By

from components.common_button import BlueButton
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

    # Локаторы...
    LABEL = (By.CSS_SELECTOR, '[class="bg-success"]')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)

        self.client_side_delay_url = PageURL(
            driver=self.driver,
            path='/clientdelay',
        )

    def check_label_text_is_present(self) -> bool:
        if self.find_and_wait_element(self.LABEL, 15):
            return self.find_and_wait_element(self.LABEL).text == 'Data calculated on the client side.'
