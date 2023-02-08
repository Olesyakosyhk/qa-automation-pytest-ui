from selenium.webdriver.support import expected_conditions as EC

from core_ui.components.component import Component


__all__ = [
    'Button',
]


class Button(Component):

    def click(
            self,
            count: int = 1,
    ) -> None:
        for i in range(count):
            self.element.click()

    def double_click(
            self,
    ) -> None:
        """
        Двойной клик
        """
        self.element.double_click()

    def click_and_hold(
            self,
    ) -> None:
        """
        Нажатие и удерживание.
        """
        self.element.click_and_hold()

    def is_clickable(self) -> bool:
        """
        Для нахождения активного элемента.
        """
        return bool(self.driver_wait.until(EC.element_to_be_clickable(self.locator)))

    def mouseover(self) -> None:
        """
        Для наведения курсора до заданной кнопки
        """
        self.action_chains.move_to_element(self.element).perform()

    def check_text(self, text: str) -> bool:
        """
        Для проверки текста кнопки.
        """
        return self.element.text == text
