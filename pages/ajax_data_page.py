from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


__all__ = [
    'AJAXDataPage',
]

from pages.mixins import BlueButtonMixin


class AJAXDataPage(BasePage, BlueButtonMixin):
    """
    Учимся ждать ответа при AJAX запросе.

    Page URL:
        http://uitestingplayground.com/ajax
    """

    # Локаторы...
    TRIGGERING_AJAX_REQUEST_BTN = (By.ID, 'ajaxButton')
    LABEL = (By.CSS_SELECTOR, '[class="bg-success"]')

    def check_label_is_present(self) -> WebElement | bool:
        return self.find_and_wait_element(self.LABEL)
