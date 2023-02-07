from selenium.webdriver.support import expected_conditions as EC

from components.component import Component


__all__ = [
    'Button',
]


class Button(Component):

    def click(self) -> None:
        self.element.click()

    def is_clickable(self) -> bool:
        """
        Для нахождения активного элемента.
        """
        return bool(self.driver_wait.until(EC.element_to_be_clickable(self.locator)))
