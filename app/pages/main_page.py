from selenium.webdriver.common.by import By

from core_ui.components.link import Link
from core_ui.page import BasePage
from core_ui.page_url import PageURL


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

        self.dynamic_id_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Dynamic ID")]',
        )
        self.class_attribute_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Class Attribute")]',
        )
        self.ajax_data_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "AJAX Data")]',
        )
        self.hidden_layers_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Hidden Layers")]',
        )
        self.load_delay_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Load Delay")]',
        )
        self.client_side_delay_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Client Side Delay")]',
        )
        self.click_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Click")]',
        )
        self.text_input_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Text Input")]',
        )
        self.scrollbars_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Scrollbars")]',
        )
        self.verify_text_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Verify Text")]',
        )
        self.dynamic_table_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Dynamic Table")]',
        )
        self.progress_bar_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Progress Bar")]',
        )
        self.visibility_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Visibility")]',
        )
        self.sample_app_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Sample App")]',
        )
        self.mouse_over_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Mouse Over")]',
        )
        self.non_breaking_space_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Non-Breaking Space")]',
        )
        self.overlapped_element_space_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Overlapped Element")]',
        )
        self.shadow_dom_link = Link(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path='//a[contains(text(), "Shadow DOM")]',
        )

        self.elements = (
            self.dynamic_id_link,
            self.class_attribute_link,
            self.ajax_data_link,
            self.hidden_layers_link,
            self.load_delay_link,
            self.client_side_delay_link,
            self.click_link,
            self.text_input_link,
            self.scrollbars_link,
            self.verify_text_link,
            self.dynamic_table_link,
            self.progress_bar_link,
            self.visibility_link,
            self.sample_app_link,
            self.mouse_over_link,
            self.non_breaking_space_link,
            self.overlapped_element_space_link,
            self.shadow_dom_link,
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
