from selenium.webdriver.common.by import By

from core_ui.components import Button
from core_ui.page import BasePage


__all__ = [
    'NonBreakingSpacePage',
]


class NonBreakingSpacePage(BasePage):
    """
    Поиск элемента с неразрывным пробелом.

    Page URL:
        http://uitestingplayground.com/nbsp
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.my_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//button[contains(text(), "My Button")]',
        )
