from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver

from core_ui.components import Component


__all__ = [
    'DragAndDrop',
]


class DragAndDrop:
    def __init__(
            self,
            driver: WebDriver,
    ) -> None:
        self.driver = driver
        self.action_chains = ActionChains(self.driver)

    def move(
            self,
            element: Component,
            target: Component,
    ) -> None:
        """
        Перетаскивание объекта.
        """
        self.action_chains.drag_and_drop(
            element.element,
            target.element,
        ).perform()
