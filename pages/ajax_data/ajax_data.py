from selenium.webdriver.common.by import By

from core.settings import BASE_URL
from pages.base import BaseUI


class AJAXData(BaseUI):
    """
    http://uitestingplayground.com/ajax
    """

    AJAX_URL = f'{BASE_URL}/ajax'

    # Локаторы...
    TRIGGERING_AJAX_REQUEST_BTN = (By.ID, 'ajaxButton')
    LABEL = (By.CSS_SELECTOR, '[class="bg-success"]')

    # Функции...
    def check_ajax_url(self) -> bool:
        return self.get_current_url() == self.AJAX_URL

    def check_label_is_present(self) -> bool:
        return self.find_and_wait_element(self.LABEL)
