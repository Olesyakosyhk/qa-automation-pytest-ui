from selenium.webdriver.common.by import By

from app.components.common_button import BlueButton
from core_ui.components import Button, Component
from core_ui.page import BasePage
from core_ui.page_url import PageURL


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

    def __init__(self, *args, **kwargs):
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

        self.progress_bar_page_url = PageURL(
            driver=self.driver,
            path='/progressbar',
        )

    def click_stop_btn(self) -> None:
        for i in range(10):
            if self.progress_bar.get_attribute('aria-valuenow') >= self.TARGET_PERCENT:
                self.click_btn(self.stop_button)
                break

    def check_result_progress_bar(self) -> bool:
        return self.progress_bar.get_attribute('aria-valuenow') >= self.TARGET_PERCENT
