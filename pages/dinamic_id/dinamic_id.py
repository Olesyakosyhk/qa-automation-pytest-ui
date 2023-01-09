from selenium.webdriver.common.by import By

from core.settings import BASE_URL
from pages.base import BaseUI


class DynamicID(BaseUI):

    DYNAMIC_ID_URL = f'{BASE_URL}/dynamicid'

    # Локатор...
    DYNAMIC_ID_BTN = (By.CSS_SELECTOR, '[class="btn btn-primary"]')

    # Функции...
    def check_configuration_form_was_successful_by_link(self) -> bool:
        return self.get_current_url() == self.DYNAMIC_ID_URL

    def check_is_present_dynamic_id_btn(self) -> bool:
        return self.is_element_present(self.DYNAMIC_ID_BTN)

    def check_is_clickable_dynamic_id_btn(self) -> bool:
        return self.is_clickable(self.DYNAMIC_ID_BTN)
