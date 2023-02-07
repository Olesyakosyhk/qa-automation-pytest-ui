from app.components.common_button import BlueButton
from core_ui.page import BasePage
from core_ui.page_url import PageURL


__all__ = [
    'LoadDelayPage',
]


class LoadDelayPage(BasePage):
    """
    Тест может ожидать загрузки страницы.

    Page URL:
        http://uitestingplayground.com/loaddelay
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)

        self.load_delay_page_url = PageURL(
            driver=self.driver,
            path='/loaddelay',
        )
