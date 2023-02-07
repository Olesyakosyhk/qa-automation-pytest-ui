from components.common_button import BlueButton, GreenButton, RedButton, YellowButton
from pages.base_page import BasePage


__all__ = [
    'VisibilityPage',
]


class VisibilityPage(BasePage):
    """
    Проверяем видимость элемента на экране.

     Page URL:
        http://uitestingplayground.com/visibility
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.blue_button = BlueButton(driver=self.driver)
        self.red_button = RedButton(driver=self.driver)
        self.yellow_button = YellowButton(driver=self.driver)
        self.green_button = GreenButton(driver=self.driver)

    def check_is_elements_present(self) -> bool:
        """
        Для нахождения списка элементов в DOM страницы.
        """
        for element in (
            self.blue_button,
            self.red_button,
            self.yellow_button,
            self.green_button,
        ):
            if element.find_and_wait_element() is False:
                return False
        return True
