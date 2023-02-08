from selenium.webdriver.support.ui import Select as SelectSelenium

from core_ui.components import Component


__all__ = [
    'Select',
]


class Select(Component):
    """
    Методы для взаимодействия с раскрывающимися списками, выбора элементов
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._select = SelectSelenium(self.element)
