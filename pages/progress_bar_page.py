from selenium.webdriver.common.by import By

from components.button import Button
from components.common_button import BlueButton
from pages.base_page import BasePage


__all__ = [
    'ProgressBarPage',
]


class ProgressBarPage(BasePage):
    """
    Отслеживаем "progress bar".

    Page URL:
        http://uitestingplayground.com/progressbar
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)

        self.stop_button = Button(
            driver=self.driver,
            locator_type=By.ID,
            locator_path='stopButton',
        )

    # Локаторы...
    PROGRESS_BAR = (By.ID, 'progressBar')

    def click_stop_btn(self) -> None:
        for i in range(10):
            progress_bar = self.find_and_wait_element(self.PROGRESS_BAR)
            value_progress_bar = progress_bar.get_attribute('aria-valuenow')
            if value_progress_bar >= '75':
                self.click_btn(self.stop_button)
                break

    def check_result_progress_bar(self) -> bool:
        progress_bar = self.find_and_wait_element(self.PROGRESS_BAR)
        value_progress_bar = progress_bar.get_attribute('aria-valuenow')
        return value_progress_bar >= '75'
