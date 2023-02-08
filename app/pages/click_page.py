from app.components.common_button import BlueButton, GreenButton
from core_ui.page import BasePage


__all__ = [
    'ClickPage',
]


class ClickPage(BasePage):
    """
    Запись нажатия кнопки.

    Page URL:
        http://uitestingplayground.com/click
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)
        self.green_button = GreenButton(driver=self.driver)
