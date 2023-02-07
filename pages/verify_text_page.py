from selenium.webdriver.common.by import By

from components.span import Span
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

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.target_text = Span(
            driver=self.driver,
            locator_type=By.CSS_SELECTOR,
            locator_path='[class="bg-primary"]>[class="badge-secondary"]',
        )
