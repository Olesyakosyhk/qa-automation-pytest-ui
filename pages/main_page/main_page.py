from selenium.webdriver.common.by import By

from core.settings import BASE_URL
from pages.base import BaseUI
from resources.enums import NamePageEnum


class MainPage(BaseUI):

    # Локаторы...
    DYNAMIC_ID_BTN = (By.XPATH, '//a[contains(text(), "Dynamic ID")]')

    CLASS_ATTRIBUTE_BTN = (By.XPATH, '//a[contains(text(), "Class Attribute")]')
    CLASS_ATTRIBUTE_URL = f'{BASE_URL}/classattr'

    AJAX_DATA_BTN = (By.XPATH, '//a[contains(text(), "AJAX Data")]')
    AJAX_URL = f'{BASE_URL}/ajax'

    HIDDEN_LAYERS_BTN = (By.XPATH, '//a[contains(text(), "Hidden Layers")]')
    HIDDEN_LAYERS_URL = f'{BASE_URL}/hiddenlayers'

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

    # Функции...
    def go_to_playground_page(self) -> None:
        self.go_to_url(self.url_base_host)

    def go_to_class_attribute_page(self) -> None:
        self.go_to_url(self.CLASS_ATTRIBUTE_URL)

    def go_to_hidden_layers_page(self) -> None:
        self.go_to_url(self.HIDDEN_LAYERS_URL)

    def go_to_page(self, name_page) -> None:
        pages = {
            NamePageEnum.DYNAMIC_ID.value: f'{BASE_URL}/dynamicid',
            NamePageEnum.CLASS_ATTRIBUTE.value: f'{BASE_URL}/classattr',
            NamePageEnum.HIDDEN_LAYERS.value: f'{BASE_URL}/hiddenlayers',
            NamePageEnum.LOAD_DELAY.value: f'{BASE_URL}/loaddelay',
            NamePageEnum.AJAX_DATA.value: f'{BASE_URL}/ajax',
            NamePageEnum.CLIENT_SIDE_DELAY.value: f'{BASE_URL}/clientdelay',
            NamePageEnum.CLICK.value: f'{BASE_URL}/click',
            NamePageEnum.TEXT_INPUT.value: f'{BASE_URL}/textinput',
            NamePageEnum.SCROLLBARS.value: f'{BASE_URL}/scrollbars',
            NamePageEnum.DYNAMIC_TABLE.value: f'{BASE_URL}/dynamictable',
            NamePageEnum.VERIFY_TEXT.value: f'{BASE_URL}/verifytext',
            NamePageEnum.PROGRESS_BAR.value: f'{BASE_URL}/progressbar',
            NamePageEnum.VISIBILITY.value: f'{BASE_URL}/visibility',
            NamePageEnum.SAMPLE_APP.value: f'{BASE_URL}/sampleapp',
            NamePageEnum.MOUSE_OVER.value: f'{BASE_URL}/mouseover',
            NamePageEnum.NON_BREAKING_SPACE.value: f'{BASE_URL}/nbsp',
            NamePageEnum.OVERLAPPED_ELEMENT.value: f'{BASE_URL}/overlapped',
            NamePageEnum.SHADOW_DOM.value: f'{BASE_URL}/shadowdom',
        }
        url_page = pages.get(name_page)
        self.go_to_url(url_page)

    def click_load_delay_btn(self) -> None:
        self.click_btn(self.LOAD_DELAY_BTN)

    # Проверки...
    def check_for_all_elements_are_visible_by_selector(self) -> bool:
        selectors = [
            self.DYNAMIC_ID_BTN,
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
            self.DYNAMIC_ID_BTN,
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
