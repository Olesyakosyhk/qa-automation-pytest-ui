from app.components.common_button import BlueButton
from core_ui.page import BasePage
from core_ui.page_url import PageURL


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
        self.scrollbars_page_url = PageURL(
            driver=self.driver,
            path='/scrollbars',
        )

    def scroll_to_blue_btn(self) -> None:
        self.scroll_page_to_element(
            element=self.blue_button.element,
        )
