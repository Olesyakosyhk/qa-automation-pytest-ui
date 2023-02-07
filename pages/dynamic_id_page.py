from components.common_button import BlueButton
from components.page_url import PageURL
from pages.base_page import BasePage


__all__ = [
    'DynamicIDPage',
]


class DynamicIDPage(BasePage):
    """
       Учимся ждать искать надежный атрибут.

       Page URL:
           http://uitestingplayground.com/dynamicid
       """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)

        self.dynamic_id_page_url = PageURL(
            driver=self.driver,
            path='/dynamicid',
        )
