from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from core_ui.components import Button, Span
from core_ui.page import BasePage
from core_ui.window import Window


__all__ = [
    'MouseOverPage',
]


class MouseOverPage(BasePage, Window):
    """
    Наведение мыши на элемент может изменить DOM и сделать элемент недоступным.

     Page URL:
        http://uitestingplayground.com/mouseover
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.action_chains = ActionChains(self.driver)

        self.original_element_btn = Button(
            driver=self.driver,
            locator_type=By.CSS_SELECTOR,
            locator_path='[class="text-primary"]',
        )
        self.modified_element_button = Button(
            driver=self.driver,
            locator_type=By.CSS_SELECTOR,
            locator_path='[class="text-warning"]',
        )
        self.counter = Span(
            driver=self.driver,
            locator_type=By.ID,
            locator_path='clickCount',
        )

    def mouseover_to_original_element_btn(self) -> None:
        self.mouseover_to_element(self.original_element_btn.element)
