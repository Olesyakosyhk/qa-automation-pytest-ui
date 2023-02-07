from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.button import Button
from components.common_button import BlueButton
from components.page_url import PageURL
from pages.base_page import BasePage


__all__ = [
    'AJAXDataPage',
]


class AJAXDataPage(BasePage):
    """
    Учимся ждать ответа при AJAX запросе.

    Page URL:
        http://uitestingplayground.com/ajax
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)

        self.triggering_ajax_request_btn = Button(
            driver=self.driver,
            locator_type=By.ID,
            locator_path='ajaxButton',
        )

        self.ajax_page_url = PageURL(
            driver=self.driver,
            path='/ajax',
        )

    # Локаторы...
    LABEL = (By.CSS_SELECTOR, '[class="bg-success"]')

    def check_label_is_present(self) -> WebElement | bool:
        return self.find_and_wait_element(self.LABEL)
