from selenium.webdriver.common.by import By

from components.button import Button
from components.page_url import PageURL
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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

        self.mouseover_page_url = PageURL(
            driver=self.driver,
            path='/mouseover',
        )
    # Локаторы...
    LINK_CLICKED = (By.ID, 'clickCount')

    def check_the_link_clicked_times(self) -> bool:
        return self.find_and_wait_element(self.LINK_CLICKED).text == '2'
