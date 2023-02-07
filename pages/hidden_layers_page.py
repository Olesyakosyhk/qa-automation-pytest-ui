from components.common_button import BlueButton, GreenButton
from components.page_url import PageURL
from pages.base_page import BasePage


__all__ = [
    'HiddenLayersPage',
]


class HiddenLayersPage(BasePage):
    """
    Тест не взаимодействует с элементами, невидимыми из-за z-порядка.

    Page URL:
        http://uitestingplayground.com/hiddenlayers
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)
        self.green_button = GreenButton(driver=self.driver)

        self.hidden_layers_page_url = PageURL(
            driver=self.driver,
            path='/hiddenlayers',
        )
