from selenium.webdriver import WebKitGTK

from app.pages.ajax_data_page import AJAXDataPage
from app.pages.class_attribute_page import ClassAttributePage
from app.pages.click_page import ClickPage
from app.pages.client_side_delay_page import ClientSideDelayPage
from app.pages.dynamic_id_page import DynamicIDPage
from app.pages.dynamictable_page import DynamicTablePage
from app.pages.hidden_layers_page import HiddenLayersPage
from app.pages.load_delay_page import LoadDelayPage
from app.pages.main_page import MainPage
from app.pages.mouse_over_page import MouseOverPage
from app.pages.non_breaking_space_page import NonBreakingSpacePage
from app.pages.overlapped_element_page import OverlappedElementPage
from app.pages.progress_bar_page import ProgressBarPage
from app.pages.sample_app_page import SampleAppPage
from app.pages.scrollbars_page import ScrollbarsPage
from app.pages.text_input_page import TextInputPage
from app.pages.verify_text_page import VerifyTextPage
from app.pages.visibility_page import VisibilityPage


__all__ = [
    'Pages',
]


class Pages:
    """
    Page URL:
        http://uitestingplayground.com/
    """

    def __init__(self, driver: WebKitGTK) -> None:
        self.main_page = MainPage(driver=driver, path='/')
        self.ajax_data_page = AJAXDataPage(driver=driver, path='/ajax')
        self.dynamic_id_page = DynamicIDPage(driver=driver, path='/dynamicid')
        self.class_attribute_page = ClassAttributePage(driver=driver, path='/classattr')
        self.hidden_layers_page = HiddenLayersPage(driver=driver, path='/hiddenlayers')
        self.load_delay_page = LoadDelayPage(driver=driver, path='/loaddelay')
        self.client_side_delay_page = ClientSideDelayPage(driver=driver, path='/clientdelay')
        self.click_page = ClickPage(driver=driver, path='/click')
        self.text_input_page = TextInputPage(driver=driver, path='/textinput')
        self.scrollbars_page = ScrollbarsPage(driver=driver, path='/scrollbars')
        self.verify_text_page = VerifyTextPage(driver=driver, path='/verifytext')
        self.progress_bar_page = ProgressBarPage(driver=driver, path='/progressbar')
        self.visibility_page = VisibilityPage(driver=driver, path='/visibility')
        self.sample_app_page = SampleAppPage(driver=driver, path='/sampleapp')
        self.mouse_over_page = MouseOverPage(driver=driver, path='/mouseover')
        self.non_breaking_space_page = NonBreakingSpacePage(driver=driver, path='/nbsp')
        self.overlapped_element_page = OverlappedElementPage(driver=driver, path='/overlapped')
        self.dynamic_table_page = DynamicTablePage(driver=driver, path='/dynamictable')
