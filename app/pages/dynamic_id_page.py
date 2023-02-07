from app.components.common_button import BlueButton
from core_ui.page import BasePage
from core_ui.page_url import PageURL


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
