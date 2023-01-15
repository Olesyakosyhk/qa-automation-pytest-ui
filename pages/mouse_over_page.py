from selenium.webdriver.common.by import By

from pages.base_page import BasePage


__all__ = [
    'MouseOverPage',
]


class MouseOverPage(BasePage):
    """
    Наведение мыши на элемент может изменить DOM и сделать элемент недоступным.

     Page URL:
        http://uitestingplayground.com/mouseover
    """

    # Локаторы...
    ORIGINAL_ELEMENT = (By.CSS_SELECTOR, '[class="text-primary"]')
    MODIFIED_ELEMENT = (By.CSS_SELECTOR, '[class="text-warning"]')
    LINK_CLICKED = (By.ID, 'clickCount')

    def click_link_for_page(self) -> None:
        self.mouseover_to_element(self.ORIGINAL_ELEMENT)
        self.click_btn(self.MODIFIED_ELEMENT)

    def click_modified_link(self) -> None:
        self.click_btn(self.MODIFIED_ELEMENT)

    def check_the_link_clicked_times(self) -> bool:
        return self.find_and_wait_element(self.LINK_CLICKED).text == '2'
