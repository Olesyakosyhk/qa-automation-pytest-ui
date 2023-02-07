from selenium.webdriver.common.action_chains import ActionChains
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

    def mouseover(self) -> None:
        """
        Для наведения курсора до заданного элемента на странице
        """
        hover = ActionChains(self.driver).move_to_element(self.element)
        hover.perform()

    def scroll(self) -> None:
        """
        Для скролла до заданной кнопки на странице
        """
        self.driver.execute_script('return arguments[0].scrollIntoView(true);', self.element)

    def check_text(self, text: str) -> bool:
        return self.element.text == text
