from selenium.webdriver.common.by import By

from pages.base import BaseUI


class MainPage(BaseUI):

    # Локаторы...
    DINAMIC_ID_BTN = (By.XPATH, '//a[contains(text(), "Dynamic ID")]')
    CLASS_ATTRIBUTE_BTN = (By.XPATH, '//a[contains(text(), "Class Attribute")]')
    HIDDEN_LAYERS_BTN = (By.XPATH, '//a[contains(text(), "Hidden Layers")]')
    LOAD_DELAY_BTN = (By.XPATH, '//a[contains(text(), "Load Delay")]')
    AJAX_DATA_BTN = (By.XPATH, '//a[contains(text(), "AJAX Data")]')
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

    # Функции...
    def go_to_playground_page(self) -> None:
        self.go_to_url(self.url_base_host)

    def click_dinamic_id_btn(self) -> None:
        self.find_and_wait_element(self.DINAMIC_ID_BTN).click()

    def click_class_attribute_btn(self) -> None:
        self.find_and_wait_element(self.CLASS_ATTRIBUTE_BTN).click()

    def click_hidden_layers_btn(self) -> None:
        self.find_and_wait_element(self.HIDDEN_LAYERS_BTN).click()

    def click_load_delay_btn(self) -> None:
        self.find_and_wait_element(self.LOAD_DELAY_BTN).click()

    def click_ajax_data_btn(self) -> None:
        self.find_and_wait_element(self.AJAX_DATA_BTN).click()

    def click_verify_text_btn(self) -> None:
        self.find_and_wait_element(self.VERIFY_TEXT_BTN).click()

    def click_progress_bar_btn(self) -> None:
        self.find_and_wait_element(self.PROGRESS_BAR_BTN).click()

    def click_visibility_btn(self) -> None:
        self.find_and_wait_element(self.VISIBILITY_BTN).click()

    def click_sample_app_btn(self) -> None:
        self.find_and_wait_element(self.SAMPLE_APP_BTN).click()

    def click_mouse_over_btn(self) -> None:
        self.find_and_wait_element(self.MOUSE_OVER_BTN).click()

    def click_non_breaking_space_btn(self) -> None:
        self.find_and_wait_element(self.NON_BREAKING_SPACE_BTN).click()

    def click_overlapped_element_btn(self) -> None:
        self.find_and_wait_element(self.OVERLAPPED_ELEMENT_BTN).click()

    def click_shadow_dom_btn(self) -> None:
        self.find_and_wait_element(self.SHADOW_DOM_BTN).click()

    # Проверки...
    def check_for_all_elements_are_visible_by_selector(self) -> bool:
        selectors = [
            self.DINAMIC_ID_BTN,
            self.CLASS_ATTRIBUTE_BTN,
            self.HIDDEN_LAYERS_BTN,
            self.LOAD_DELAY_BTN,
            self.AJAX_DATA_BTN,
            self.TEXT_INPUT_BTN,
            self.SCROLLBARS_BTN,
            self.DYNAMIC_TABLE_BTN,
            self.VERIFY_TEXT_BTN,
            self.PROGRESS_BAR_BTN,
            self.VISIBILITY_BTN,
            self.SAMPLE_APP_BTN,
            self.MOUSE_OVER_BTN,
            self.NON_BREAKING_SPACE_BTN,
            self.OVERLAPPED_ELEMENT_BTN,
            self.SHADOW_DOM_BTN,
        ]
        return self.wait_for_all_elements_are_visible_by_selector(selector_array=selectors)

    def check_element_is_clickable(self) -> bool:
        locators_array = [
            self.DINAMIC_ID_BTN,
            self.CLASS_ATTRIBUTE_BTN,
            self.HIDDEN_LAYERS_BTN,
            self.LOAD_DELAY_BTN,
            self.AJAX_DATA_BTN,
            self.TEXT_INPUT_BTN,
            self.SCROLLBARS_BTN,
            self.DYNAMIC_TABLE_BTN,
            self.VERIFY_TEXT_BTN,
            self.PROGRESS_BAR_BTN,
            self.VISIBILITY_BTN,
            self.SAMPLE_APP_BTN,
            self.MOUSE_OVER_BTN,
            self.NON_BREAKING_SPACE_BTN,
            self.OVERLAPPED_ELEMENT_BTN,
            self.SHADOW_DOM_BTN,
        ]
        return self.is_clickable_elements(locators_array=locators_array)
