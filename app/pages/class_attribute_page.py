from app.components.common_button import BlueButton, GreenButton, YellowButton
from core_ui.page import BasePage


__all__ = [
    'ClassAttributePage',
]


class ClassAttributePage(BasePage):
    """
    Поиск основной кнопки, появляющейся рандомно среди других кнопок.

    Page URL:
        http://uitestingplayground.com/classattr
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)
        self.yellow_button = YellowButton(driver=self.driver)
        self.green_button = GreenButton(driver=self.driver)

    def accept_alert(self) -> None:
        alert = self.switch_to_alert()
        alert.accept()
