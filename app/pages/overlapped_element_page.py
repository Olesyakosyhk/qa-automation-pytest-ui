from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from core_ui.components import Input
from core_ui.page import BasePage
from core_ui.window import Window


__all__ = [
    'OverlappedElementPage',
]


class OverlappedElementPage(BasePage, Window):
    """
    Сделать элемент видимым для ввода текста.

    Page URL:
        http://uitestingplayground.com/overlapped
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.action_chains = ActionChains(self.driver)

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
