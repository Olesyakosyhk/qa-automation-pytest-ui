from components.common_button import BlueButton
from pages.base_page import BasePage
from resources.common_locators import CommonLocators


__all__ = [
    'ScrollbarsPage',
]


class ScrollbarsPage(BasePage):
    """
    Учимся скроллить до нужного элемента на странице.

    Page URL:
        http://uitestingplayground.com/scrollbars
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)

    def scroll_to_blue_btn(self) -> None:
        self.page_scroll_to_locator(CommonLocators.BLUE_BTN)
