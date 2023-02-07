from selenium.webdriver.common.by import By

from components.button import Button
from components.page_url import PageURL
from pages.base_page import BasePage


__all__ = [
    'MainPage',
]


class MainPage(BasePage):
    """
        Проверки на главной странице сайта.

        Page URL:
            http://uitestingplayground.com/
        """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.dynamic_id_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Dynamic ID")]',
        )
        self.class_attribute_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Class Attribute")]',
        )
        self.ajax_data_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "AJAX Data")]',
        )
        self.hidden_layers_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Hidden Layers")]',
        )
        self.load_delay_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Load Delay")]',
        )
        self.client_side_delay_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Client Side Delay")]',
        )
        self.click_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Click")]',
        )
        self.text_input_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Text Input")]',
        )
        self.scrollbars_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Scrollbars")]',
        )
        self.verify_text_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Verify Text")]',
        )
        self.dynamic_table_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Dynamic Table")]',
        )
        self.progress_bar_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Progress Bar")]',
        )
        self.visibility_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Visibility")]',
        )
        self.sample_app_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Sample App")]',
        )
        self.mouse_over_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Mouse Over")]',
        )
        self.non_breaking_space_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Non-Breaking Space")]',
        )
        self.overlapped_element_space_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Overlapped Element")]',
        )
        self.shadow_dom_button = Button(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Shadow DOM")]',
        )

        self.elements = (
            self.dynamic_id_button,
            self.class_attribute_button,
            self.ajax_data_button,
            self.hidden_layers_button,
            self.load_delay_button,
            self.client_side_delay_button,
            self.click_button,
            self.text_input_button,
            self.scrollbars_button,
            self.verify_text_button,
            self.dynamic_table_button,
            self.progress_bar_button,
            self.visibility_button,
            self.sample_app_button,
            self.mouse_over_button,
            self.non_breaking_space_button,
            self.overlapped_element_space_button,
            self.shadow_dom_button,
        )

        self.main_page_url = PageURL(
            driver=self.driver,
            path='/',
        )

    def check_for_all_elements_are_visible_by_selector(self) -> bool:
        """
        Для нахождения списка элементов в DOM страницы.
        """
        for element in self.elements:
            if element.find_and_wait_element() is False:
                return False

        return True

    def check_element_is_clickable(self) -> bool:
        """
        Для нахождения списка активных элементов.
        """
        for element in self.elements:
            if not element.is_clickable():
                return False

        return True
