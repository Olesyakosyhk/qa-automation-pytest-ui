from typing import Optional

from selenium.webdriver import WebKitGTK
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core import settings


class BaseUI:

    def __init__(self, driver: WebKitGTK):
        self.driver = driver
        self.driver_wait = WebDriverWait(self.driver, timeout=settings.WEB_DRIVER_WAIT_TIMEOUT)

        self.url_base_host = settings.BASE_URL

    def _get_web_driver_wait(self, timeout: Optional[int] = None) -> WebDriverWait:
        if timeout is not None and timeout != settings.WEB_DRIVER_WAIT_TIMEOUT:
            return WebDriverWait(driver=self.driver, timeout=timeout)
        else:
            return self.driver_wait

    def find_and_wait_element(self, locator, timeout: Optional[int] = None):
        """
        Для нахождения видимого элемента в DOM страницы.
        """
        web_driver_wait: WebDriverWait = self._get_web_driver_wait(timeout=timeout)

        return web_driver_wait.until(
            method=EC.visibility_of_element_located(locator),
            message=f'Can\'t find element by locator {locator}',
        )

    def find_and_wait_elements(self, locator, timeout: Optional[int] = None):
        web_driver_wait: WebDriverWait = self._get_web_driver_wait(timeout=timeout)

        return web_driver_wait.until(
            method=EC.visibility_of_all_elements_located(locator),
            message=f'Can\'t find elements by locator {locator}',
        )

    def find_and_wait_invisibility_element(self, locator, timeout: Optional[int] = None):
        """
        Для нахождения невидимого элемента на странице.
        """
        web_driver_wait: WebDriverWait = self._get_web_driver_wait(timeout=timeout)

        return web_driver_wait.until(
            method=EC.invisibility_of_element_located(locator),
            message=f'Can\'t find elements by locator {locator}',
        )

    def find_clickable_element(self, locator, timeout: int = 5):
        """
        Для нахождения активного элемента на странице.
        """
        web_driver_wait: WebDriverWait = self._get_web_driver_wait(timeout=timeout)

        return web_driver_wait.until(
            method=EC.element_to_be_clickable(locator),
            message=f'Can\'t click element on the page {locator}',
        )

    def find_staleness_of_element(self, element, timeout: int = 40):
        """
        Для определения отсутствия элемента, ранее присутствующего в DOM страницы.
        """
        web_driver_wait: WebDriverWait = self._get_web_driver_wait(timeout=timeout)

        return web_driver_wait.until(
            method=EC.staleness_of(element),
            message=f'Can\'t click element on the page {element}',
        )

    def wait_for_all_elements_staleness_of(self, selector_array: list) -> bool:
        """
        Для определения отсутствия списка элементов, ранее присутствующего в DOM страницы.
        """
        result = True
        for selector in selector_array:
            if self.find_staleness_of_element(selector) is False:
                result = False
                break

        return result

    def wait_for_all_elements_are_visible_by_selector(self, selector_array: list) -> bool:
        """
        Для нахождения списка элементов в DOM страницы.
        """
        result = True

        for selector in selector_array:
            if self.find_and_wait_element(selector) is False:
                result = False
                break

        return result

    def is_elements_not_present(self, selector_array: list,  timeout: Optional[int] = None) -> bool:
        """
        Для нахождения списка отсутствующих элементов.
        """
        result = True

        for selector in selector_array:
            if self.find_and_wait_element(selector, timeout=timeout) is False:
                result = False
                break

        return result

    def is_checked_elements_is_not_selected(self, locators_array: list) -> bool:
        """
        Для нахождения из списка локаторов не выбранных элементов.(no click)
        """
        result = True
        for locator in locators_array:
            locator_selected = self.find_and_wait_invisibility_element(locator)
            if locator_selected.is_selected():
                result = False
                break

        return result

    def is_checked_element_is_not_selected(self, locator) -> bool:
        """
        Для нахождения НЕ выбранного элемента.
        """
        result = True
        locator_selected = self.find_and_wait_invisibility_element(locator)
        if locator_selected.is_selected():
            result = False

        return result

    def switch_to_frame(self, name_of_frame) -> None:
        """
        Для переключения фрейм.
        """
        self.driver_wait.until(EC.frame_to_be_available_and_switch_to_it(name_of_frame))

    def switch_to_alert(self):
        """
        Для переключения alert.
        """
        return self.driver.switch_to.alert

    def is_clickable(self, _tuple) -> bool:
        """
        Для нахождения активного элемента.
        """
        result = True

        if self.driver_wait.until(EC.element_to_be_clickable(_tuple)) is False:
            result = False

        return result

    def is_clickable_elements(self, locators_array: list) -> bool:
        """
        Для нахождения списка активных элементов.
        """
        result = True
        for locator in locators_array:
            if not self.driver_wait.until(EC.element_to_be_clickable(locator)):
                result = False
                break

        return result

    def is_element_not_present(self, _tuple) -> bool:
        """
        Дл определения ОТСУТСТВИЯ элемента в DOM страницы.
        """
        if self.find_and_wait_element(_tuple):
            result = False
        else:
            result = True

        return result

    def is_element_present(self, _tuple):
        """
        Для нахождения видимого элемента в DOM страницы.
        """
        result = True
        if self.find_and_wait_element(_tuple) is False:
            result = False

        return result

    def click_btn(self, locator) -> None:
        btn = self.find_and_wait_element(locator)
        btn.click()

    def get_current_url(self) -> str:
        """
        Для определения текущего УРЛ.
        """
        return self.driver.current_url

    def get_title_text(self) -> str:
        return self.driver.title

    def go_to_url(self, full_url: str) -> None:
        self.driver.get(full_url)

    def is_element_invisible(self, locator, delay=1):
        return WebDriverWait(self.driver, delay).until(
            method=EC.invisibility_of_element_located(locator),
            message=f'Can\'t find element by locator {locator}',
        )

    def page_scroll_to_locator(self, locator) -> None:
        """
        Для скролла до заданного элемента на странице
        """
        element = self.find_and_wait_element(locator)
        self.driver.execute_script('return arguments[0].scrollIntoView(true);', element)

    def switch_to_window(self, window_name):
        """
        Для переключения вкладки в браузере.
        """
        self.driver.switch_to.window(window_name)
