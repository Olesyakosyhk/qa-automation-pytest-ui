from components.common_button import BlueButton
from components.page_url import PageURL
from pages.base_page import BasePage


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
