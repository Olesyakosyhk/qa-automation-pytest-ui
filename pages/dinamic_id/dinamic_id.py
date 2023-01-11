from core.settings import BASE_URL
from pages.base import BaseUI
from resources.common_locators import CommonLocators


class DynamicID(BaseUI):

    DYNAMIC_ID_URL = f'{BASE_URL}/dynamicid'

    # Функции...
    def check_configuration_form_was_successful_by_link(self) -> bool:
        return self.get_current_url() == self.DYNAMIC_ID_URL

    def check_is_present_dynamic_id_btn(self) -> bool:
        return self.is_element_present(CommonLocators.BLUE_BTN)

    def check_is_clickable_dynamic_id_btn(self) -> bool:
        return self.is_clickable(CommonLocators.BLUE_BTN)
