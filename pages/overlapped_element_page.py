from selenium.webdriver.common.by import By

from pages.base_page import BasePage


__all__ = [
    'OverlappedElementPage',
]


class OverlappedElementPage(BasePage):
    """
    Сделать элемент видимым для ввода текста.

    Page URL:
        http://uitestingplayground.com/overlapped
    """

    # Локаторы...
    ID_INPUT = (By.ID, 'id')
    NAME_INPUT = (By.ID, 'name')

    def set_id(self, numb_id: str) -> None:
        self.find_and_wait_element(self.ID_INPUT).send_keys(numb_id)

    def scroll_to_name_input(self) -> None:
        self.page_scroll_to_locator(self.NAME_INPUT)

    def set_name(self, name: str) -> None:
        self.find_and_wait_element(self.NAME_INPUT).send_keys(name)
