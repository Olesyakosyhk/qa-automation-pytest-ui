from typing import Optional

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from components.types import LocatorType
from core import settings


__all__ = [
    'BasePage'
]


class BasePage:

    def __init__(
            self,
            driver: WebDriver,
            path: str,
    ) -> None:
        self.driver = driver
        self.driver_wait = WebDriverWait(self.driver, timeout=settings.WEB_DRIVER_WAIT_TIMEOUT)

        self.base_url = settings.BASE_URL
        self.page_url = f'{self.base_url}{path}'

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

    def find_and_wait_invisibility_element(self, locator, timeout: Optional[int] = None):
        """
        Для нахождения невидимого элемента на странице.
        """
        web_driver_wait: WebDriverWait = self._get_web_driver_wait(timeout=timeout)

        return web_driver_wait.until(
            method=EC.invisibility_of_element_located(locator),
            message=f'Can\'t find elements by locator {locator}',
        )

    def find_staleness_of_element(self, element, timeout: int = 40):
        """
        Для определения отсутствия элемента, ранее присутствующего в DOM страницы.
        """
        web_driver_wait: WebDriverWait = self._get_web_driver_wait(timeout=timeout)

        return web_driver_wait.until(
            method=EC.staleness_of(element),
            message=f'Can\'t find element on the page {element}',
        )

    def find_text_to_be_present_in_element(self, element, text: str, timeout: Optional[int] = None):
        """
        Для определения отсутствия элемента, ранее присутствующего в DOM страницы.
        """
        web_driver_wait: WebDriverWait = self._get_web_driver_wait(timeout=timeout)

        return web_driver_wait.until(
            method=EC.text_to_be_present_in_element(element, text),
            message=f'Can\'t find element on the page {element}',
        )

    def wait_for_all_elements_are_visible_by_selector(self, selector_array: list | tuple) -> bool:
        """
        Для нахождения списка элементов в DOM страницы.
        """
        result = True

        for selector in selector_array:
            if self.find_and_wait_element(selector) is False:
                result = False
                break

        return result

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

    def is_clickable_elements(self, locators_array: list | tuple) -> bool:
        """
        Для нахождения списка активных элементов.
        """
        result = True
        for locator in locators_array:
            if not self.driver_wait.until(EC.element_to_be_clickable(locator)):
                result = False
                break

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

    def go_to_url(self, full_url: str) -> None:
        self.driver.get(full_url)

    def go_to_page(self) -> None:
        self.go_to_url(self.page_url)

    def scroll_page_to_element(self, element) -> None:
        """
        Для скролла до заданного элемента на странице
        """
        self.driver.execute_script(
            'return arguments[0].scrollIntoView(true);',
            element,
        )

    def scroll_page_to_locator(
            self,
            locator: tuple[LocatorType, str],
    ) -> None:
        """
        Для скролла до заданного элемента на странице
        """
        self.scroll_page_to_element(
            element=self.find_and_wait_element(locator),
        )

    def mouseover_to_element(self, locator) -> None:
        """
        Для наведения курсора до заданного элемента на странице
        """
        element = self.find_and_wait_element(locator)

        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def check_url(self) -> bool:
        """
        Проверка url страницы
        """
        return self.get_current_url() == self.page_url
