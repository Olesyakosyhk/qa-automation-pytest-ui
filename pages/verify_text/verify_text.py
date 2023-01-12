from selenium.webdriver.common.by import By

from pages.base import BaseUI


class VerifyText(BaseUI):
    """
    http://uitestingplayground.com/verifytext
    """
    # Локатор...
    TEXT = (By.CSS_SELECTOR, '[class="bg-primary"]>[class="badge-secondary"]')

    # Функции...
    def check_finds_an_element(self) -> bool:
        return self.find_and_wait_element(self.TEXT).text == 'Welcome UserName!'
