from pages.ajax_data.ajax_data import AJAXData
from pages.class_attribute.class_attribute import ClassAttribute
from pages.dinamic_id.dinamic_id import DynamicID
from pages.main_page.main_page import MainPage


class PlaygroundPage:
    def __init__(self, browser):
        self.main_page = MainPage(driver=browser)
        self.ajax_data = AJAXData(driver=browser)
        self.dynamic_id = DynamicID(driver=browser)
        self.class_attribute = ClassAttribute(driver=browser)
