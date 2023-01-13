from selenium.webdriver.common.by import By

from pages.base import BaseUI


class OverlappedElement(BaseUI):
    """
    http://uitestingplayground.com/overlapped
    """

    # Локаторы...
    ID_INPUT = (By.ID, 'id')
    NAME_INPUT = (By.ID, 'name')

    # Функции...
    def set_id(self, numb_id) -> None:
        self.find_and_wait_element(self.ID_INPUT).send_keys(numb_id)

    def scroll_to_name_input(self):
        self.page_scroll_to_locator(self.NAME_INPUT)

    def set_name(self, name) -> None:
        self.find_and_wait_element(self.NAME_INPUT).send_keys(name)
