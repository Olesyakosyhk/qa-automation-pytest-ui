from selenium.webdriver.common.by import By

from pages.base_page import BasePage


__all__ = [
    'ProgressBarPage',
]

from pages.mixins import BlueButtonMixin


class ProgressBarPage(BasePage, BlueButtonMixin):
    """
    Отслеживаем "progress bar".

    Page URL:
        http://uitestingplayground.com/progressbar
    """

    # Локаторы...
    STOP_BTN = (By.ID, 'stopButton')
    PROGRESS_BAR = (By.ID, 'progressBar')

    def click_stop_btn(self) -> None:
        for i in range(10):
            progress_bar = self.find_and_wait_element(self.PROGRESS_BAR)
            value_progress_bar = progress_bar.get_attribute('aria-valuenow')
            if value_progress_bar >= '75':
                self.click_btn(self.STOP_BTN)
                break

    def check_result_progress_bar(self) -> bool:
        progress_bar = self.find_and_wait_element(self.PROGRESS_BAR)
        value_progress_bar = progress_bar.get_attribute('aria-valuenow')
        return value_progress_bar >= '75'
