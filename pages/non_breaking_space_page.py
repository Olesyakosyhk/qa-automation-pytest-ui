from selenium.webdriver.common.by import By

from components.button import Button
from components.page_url import PageURL
from pages.base_page import BasePage


__all__ = [
    'NonBreakingSpacePage',
]


class NonBreakingSpacePage(BasePage):
    """
    Поиск элемента с неразрывным пробелом.

    Page URL:
        http://uitestingplayground.com/nbsp
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.my_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//button[contains(text(), "My Button")]',
        )

        self.nbsp_page_url = PageURL(
            driver=self.driver,
            path='/nbsp',
        )
