from pages.ajax_data.ajax_data import AJAXData
from pages.class_attribute.class_attribute import ClassAttribute
from pages.click.click import ClickPage
from pages.client_side_delay.client_side_delay import ClientSideDelay
from pages.common_methods import CommonMethods
from pages.dinamic_id.dinamic_id import DynamicID
from pages.hidden_layers.hidden_layers import HiddenLayers
from pages.load_delay.load_delay import LoadDelay
from pages.main_page.main_page import MainPage
from pages.scrollbars.scrollbars import ScrollbarsPage
from pages.text_input.text_input import TextInput


class PlaygroundPage:
    def __init__(self, browser):
        self.common_methods = CommonMethods(driver=browser)
        self.main_page = MainPage(driver=browser)
        self.ajax_data = AJAXData(driver=browser)
        self.dynamic_id = DynamicID(driver=browser)
        self.class_attribute = ClassAttribute(driver=browser)
        self.hidden_layers = HiddenLayers(driver=browser)
        self.load_delay = LoadDelay(driver=browser)
        self.client_side_delay = ClientSideDelay(driver=browser)
        self.click_page = ClickPage(driver=browser)
        self.text_input = TextInput(driver=browser)
        self.scrollbars = ScrollbarsPage(driver=browser)
