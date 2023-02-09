from app.components.common_button import BlueButton
from core_ui.page import BasePage
from core_ui.window import Window


__all__ = [
    'ScrollbarsPage',
]


class ScrollbarsPage(BasePage, Window):
    """
    Учимся скроллить до нужного элемента на странице.

    Page URL:
        http://uitestingplayground.com/scrollbars
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)

    def scroll_to_blue_btn(self) -> None:
        self.scroll_page_to_element(
            element=self.blue_button.element,
        )
