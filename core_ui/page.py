from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core import settings
from core_ui.page_url import PageURL
from core_ui.resources.types import Locator


__all__ = [
    'BasePage'
]


class BasePage(PageURL):

    def __init__(
            self,
            driver: WebDriver,
            path: str,
    ) -> None:
        self.driver = driver
        self.driver_wait = WebDriverWait(self.driver, timeout=settings.WEB_DRIVER_WAIT_TIMEOUT)

        self.base_url = settings.BASE_URL
        self.page_url = f'{self.base_url}{path}'

    def _get_web_driver_wait(
            self,
            timeout: Optional[int] = None,
    ) -> WebDriverWait:
        if timeout is not None and timeout != settings.WEB_DRIVER_WAIT_TIMEOUT:
            return WebDriverWait(
                driver=self.driver,
                timeout=timeout,
            )
        else:
            return self.driver_wait

    def find_and_wait_element(
            self,
            locator: Locator,
            timeout: Optional[int] = None,
    ) -> WebElement:
        """
        Для нахождения видимого элемента в DOM страницы.
        """
        web_driver_wait: WebDriverWait = self._get_web_driver_wait(timeout=timeout)

        return web_driver_wait.until(
            method=EC.visibility_of_element_located(locator),
            message=f'Can\'t find element by locator {locator}',
        )

    def find_and_wait_invisibility_element(
            self,
            locator: Locator,
            timeout: Optional[int] = None,
    ) -> WebElement:
        """
        Для нахождения невидимого элемента на странице.
        """
        web_driver_wait: WebDriverWait = self._get_web_driver_wait(timeout=timeout)

        return web_driver_wait.until(
            method=EC.invisibility_of_element_located(locator),
            message=f'Can\'t find elements by locator {locator}',
        )

    def find_staleness_of_element(
            self,
            element: WebElement,
            timeout: int = 20,
    ) -> WebElement:
        """
        Для определения отсутствия элемента, ранее присутствующего в DOM страницы.
        """
        web_driver_wait: WebDriverWait = self._get_web_driver_wait(timeout=timeout)

        return web_driver_wait.until(
            method=EC.staleness_of(element),
            message=f'Can\'t find element on the page {element}',
        )

    def find_text_to_be_present_in_element(
            self,
            element: WebElement,
            text: str,
            timeout: Optional[int] = None,
    ) -> bool:
        """
        Проверка наличия текста в элементе.
        """
        web_driver_wait: WebDriverWait = self._get_web_driver_wait(timeout=timeout)

        return web_driver_wait.until(
            method=EC.text_to_be_present_in_element(element, text),
            message=f'Can\'t find element on the page {element}',
        )
