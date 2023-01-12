from selenium.webdriver.common.by import By

from pages.base import BaseUI


class ProgressBar(BaseUI):
    """
    http://uitestingplayground.com/progressbar
    """

    # Локаторы...
    STOP_BTN = (By.ID, 'stopButton')
    PROGRESS_BAR = (By.ID, 'progressBar')

    # Функции...
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
