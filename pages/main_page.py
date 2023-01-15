from selenium.webdriver.common.by import By

from pages.base_page import BasePage


__all__ = [
    'MainPage',
]


class MainPage(BasePage):

    # Локаторы...
    DYNAMIC_ID_BTN = (By.XPATH, '//a[contains(text(), "Dynamic ID")]')
    CLASS_ATTRIBUTE_BTN = (By.XPATH, '//a[contains(text(), "Class Attribute")]')
    AJAX_DATA_BTN = (By.XPATH, '//a[contains(text(), "AJAX Data")]')
    HIDDEN_LAYERS_BTN = (By.XPATH, '//a[contains(text(), "Hidden Layers")]')
    LOAD_DELAY_BTN = (By.XPATH, '//a[contains(text(), "Load Delay")]')
    CLICK_BTN = (By.XPATH, '//a[contains(text(), "Click")]')
    TEXT_INPUT_BTN = (By.XPATH, '//a[contains(text(), "Text Input")]')
    SCROLLBARS_BTN = (By.XPATH, '//a[contains(text(), "Scrollbars")]')
    DYNAMIC_TABLE_BTN = (By.XPATH, '//a[contains(text(), "Dynamic Table")]')
    VERIFY_TEXT_BTN = (By.XPATH, '//a[contains(text(), "Verify Text")]')
    PROGRESS_BAR_BTN = (By.XPATH, '//a[contains(text(), "Progress Bar")]')
    VISIBILITY_BTN = (By.XPATH, '//a[contains(text(), "Visibility")]')
    SAMPLE_APP_BTN = (By.XPATH, '//a[contains(text(), "Sample App")]')
    MOUSE_OVER_BTN = (By.XPATH, '//a[contains(text(), "Mouse Over")]')
    NON_BREAKING_SPACE_BTN = (By.XPATH, '//a[contains(text(), "Non-Breaking Space")]')
    OVERLAPPED_ELEMENT_BTN = (By.XPATH, '//a[contains(text(), "Overlapped Element")]')
    SHADOW_DOM_BTN = (By.XPATH, '//a[contains(text(), "Shadow DOM")]')

    SELECTORS = (
        DYNAMIC_ID_BTN,
        CLASS_ATTRIBUTE_BTN,
        HIDDEN_LAYERS_BTN,
        LOAD_DELAY_BTN,
        AJAX_DATA_BTN,
        TEXT_INPUT_BTN,
        SCROLLBARS_BTN,
        DYNAMIC_TABLE_BTN,
        VERIFY_TEXT_BTN,
        PROGRESS_BAR_BTN,
        VISIBILITY_BTN,
        SAMPLE_APP_BTN,
        MOUSE_OVER_BTN,
        NON_BREAKING_SPACE_BTN,
        OVERLAPPED_ELEMENT_BTN,
        SHADOW_DOM_BTN,
    )

    def click_load_delay_btn(self) -> None:
        self.click_btn(self.LOAD_DELAY_BTN)

    # Проверки...
    def check_for_all_elements_are_visible_by_selector(self) -> bool:
        return self.wait_for_all_elements_are_visible_by_selector(selector_array=self.SELECTORS)

    def check_element_is_clickable(self) -> bool:
        return self.is_clickable_elements(locators_array=self.SELECTORS)
