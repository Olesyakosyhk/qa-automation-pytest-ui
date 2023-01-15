from resources.common_locators import CommonLocators


__all__ = [
    'BlueButtonMixin',
]


class BlueButtonMixin:
    def click_btn(self, *args, **kwargs) -> None: pass

    # Нажатие синей кнопки...
    def click_blue_btn(self) -> None:
        self.click_btn(CommonLocators.BLUE_BTN)
