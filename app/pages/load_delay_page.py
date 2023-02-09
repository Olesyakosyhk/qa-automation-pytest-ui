from app.components.common_button import BlueButton
from core_ui.page import BasePage


__all__ = [
    'LoadDelayPage',
]


class LoadDelayPage(BasePage):
    """
    Тест может ожидать загрузки страницы.

    Page URL:
        http://uitestingplayground.com/loaddelay
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)
