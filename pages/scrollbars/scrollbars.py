from pages.base import BaseUI
from resources.common_locators import CommonLocators


class ScrollbarsPage(BaseUI):
    """
    http://uitestingplayground.com/scrollbars
    """

    # Функции...
    def scroll_to_blue_btn(self) -> None:
        self.page_scroll_to_locator(CommonLocators.BLUE_BTN)
