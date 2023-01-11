from selenium.webdriver.common.by import By

from core.settings import BASE_URL
from pages.base import BaseUI


class ClientSideDelay(BaseUI):
    """
    http://uitestingplayground.com/clientdelay
    """

    CLIENT_SIDE_DELAY_URL = f'{BASE_URL}/clientdelay'

    # Локаторы...
    BLUE_BTN = (By.ID, 'ajaxButton')
    LABEL = (By.CSS_SELECTOR, '[class="bg-success"]')

    # Функции...
    def go_to_client_delay_page(self) -> None:
        self.go_to_url(self.CLIENT_SIDE_DELAY_URL)

    def click_blue_btn(self) -> None:
        self.click_btn(self.BLUE_BTN)

    def check_label_text_is_present(self) -> bool:
        if self.find_and_wait_element(self.LABEL, 15):
            return self.find_and_wait_element(self.LABEL).text == 'Data calculated on the client side.'
