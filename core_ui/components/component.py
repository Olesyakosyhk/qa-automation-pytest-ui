from typing import Any

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core import settings
from core_ui.resources.types import LocatorType


__all__ = [
    'Component',
]


class Component:
    LOCATOR_TYPE: LocatorType | None = None
    LOCATOR_PATH: str | None = None

    def __init__(
            self,
            driver: WebDriver,
            locator_type: LocatorType | None = None,
            locator_path: str | None = None,
    ) -> None:
        self.locator_type: LocatorType = locator_type or self.LOCATOR_TYPE
        self.locator_path: str = locator_path or self.LOCATOR_PATH

        assert self.locator_type is not None, 'Необходимо указать `locator_type`'
        assert self.locator_path is not None, 'Необходимо указать `locator_path`'

        self.driver = driver
        self.driver_wait = WebDriverWait(
            driver=self.driver,
            timeout=settings.WEB_DRIVER_WAIT_TIMEOUT,
        )
        self.action_chains = ActionChains(self.driver)

        self._locator = (
            self.locator_type,
            self.locator_path,
        )

        self._element: Any = None

    def _get_web_driver_wait(
            self,
            timeout: int | None = None,
    ) -> WebDriverWait:
        if timeout is not None and timeout != settings.WEB_DRIVER_WAIT_TIMEOUT:
            return WebDriverWait(driver=self.driver, timeout=timeout)
        return self.driver_wait

    @property
    def locator(self) -> tuple[LocatorType, str]:
        return self._locator

    @property
    def element(self) -> Any:
        if self._element is None:
            self._element = self.find_and_wait_element()
        return self._element

    def find_and_wait_element(
            self,
            timeout: int | None = None,
    ) -> Any:
        """
        Для нахождения видимого элемента в DOM страницы.
        """
        web_driver_wait: WebDriverWait = self._get_web_driver_wait(timeout=timeout)

        self._element = web_driver_wait.until(
            method=EC.visibility_of_element_located(self.locator),
            message=f'Can\'t find element by locator {self.locator}',
        )
        return self._element

    def find_and_wait_invisibility_element(
            self,
            timeout: int | None = None,
    ) -> WebElement | bool:
        """
        Для нахождения невидимого элемента на странице.
        """
        web_driver_wait: WebDriverWait = self._get_web_driver_wait(timeout=timeout)

        return web_driver_wait.until(
            method=EC.invisibility_of_element_located(self.locator),
            message=f'Can\'t find invisibility elements by locator {self.locator}',
        )

    def find_staleness_of_element(
            self,
            timeout: int | None = None,
    ) -> WebElement | bool:
        """
        Для определения отсутствия элемента, ранее присутствующего в DOM страницы.
        """
        web_driver_wait: WebDriverWait = self._get_web_driver_wait(timeout=timeout)

        return web_driver_wait.until(
            method=EC.staleness_of(self.element),
            message=f'Can\'t find staleness element on the page {self.element}',
        )

    def find_text_to_be_present_in_element(
            self,
            text: str,
            timeout: int | None = None,
    ) -> WebElement | bool:
        """
        Для определения текста в элементе.
        """
        web_driver_wait: WebDriverWait = self._get_web_driver_wait(timeout=timeout)

        return web_driver_wait.until(
            method=EC.text_to_be_present_in_element(self.locator, text),
            message=f'Can\'t find element on the page {self.locator}',
        )

    def get_attribute(self, name: str) -> str:
        """
        Получение значения по атрибуту элемента
        """
        return self.element.get_attribute(name)

    def check_text(self, text: str) -> bool:
        """
        Проверка текста
        """
        return self.element.text == text
