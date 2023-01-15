from selenium.webdriver.common.by import By

from pages.base_page import BasePage


__all__ = [
    'VerifyTextPage',
]


class VerifyTextPage(BasePage):
    """
    Учимся находить элемент с текстом.

     Page URL:
        http://uitestingplayground.com/verifytext
    """
    # Локатор...
    TEXT = (By.CSS_SELECTOR, '[class="bg-primary"]>[class="badge-secondary"]')

    def check_finds_an_element(self) -> bool:
        return self.find_and_wait_element(self.TEXT).text == 'Welcome UserName!'
