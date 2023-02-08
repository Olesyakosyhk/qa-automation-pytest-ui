from selenium.webdriver.common.by import By

from core_ui.components import Input
from core_ui.page import BasePage


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
