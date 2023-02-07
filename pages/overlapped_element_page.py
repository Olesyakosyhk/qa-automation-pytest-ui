from selenium.webdriver.common.by import By

from components.input import Input
from components.page_url import PageURL
from pages.base_page import BasePage


__all__ = [
    'OverlappedElementPage',
]


class OverlappedElementPage(BasePage):
    """
    Сделать элемент видимым для ввода текста.

    Page URL:
        http://uitestingplayground.com/overlapped
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.overlapped_page_url = PageURL(
            driver=self.driver,
            path='/overlapped',
        )

        self.input_id = Input(
            driver=self.driver,
            locator_type=By.ID,
            locator_path='id',
        )
        self.input_name = Input(
            driver=self.driver,
            locator_type=By.ID,
            locator_path='name',
        )
