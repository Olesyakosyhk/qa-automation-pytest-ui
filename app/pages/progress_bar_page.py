from selenium.webdriver.common.by import By

from app.components.common_button import BlueButton
from core_ui.components import Button, Component
from core_ui.page import BasePage


__all__ = [
    'ProgressBarPage',
]


class ProgressBarPage(BasePage):
    """
    Отслеживаем "progress bar".

    Page URL:
        http://uitestingplayground.com/progressbar
    """
    TARGET_PERCENT = '75'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)
        self.stop_button = Button(
            driver=self.driver,
            locator_type=By.ID,
            locator_path='stopButton',
        )
        self.progress_bar = Component(
            driver=self.driver,
            locator_type=By.ID,
            locator_path='progressBar',
        )

    def click_stop_btn(self) -> None:
        progress_bar = 0
        while progress_bar <= int(self.TARGET_PERCENT):
            progress_bar = int(self.progress_bar.get_attribute('aria-valuenow'))
        self.stop_button.click()

    def check_result_progress_bar(self) -> bool:
        return self.progress_bar.get_attribute('aria-valuenow') >= self.TARGET_PERCENT
