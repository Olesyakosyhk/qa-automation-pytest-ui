from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core import settings
from core_ui.components import Component
from core_ui.resources.types import Locator


__all__ = [
    'Window',
]


class Window:
    def __init__(
            self,
            driver: WebDriver,
    ) -> None:
        self.driver = driver
        self.driver_wait = WebDriverWait(
            driver=self.driver,
            timeout=settings.WEB_DRIVER_WAIT_TIMEOUT,
        )
        self.action_chains = ActionChains(self.driver)

    def refresh(self) -> None:
        """
        Обновление страницы
        """
        self.driver.refresh()

    def add_windows_page(self, full_url: str) -> None:
        """
        Для открытия новой вкладки в браузере.
        """
        self.driver.execute_script(f'window.open("{full_url}")')

    def switch_to_window_handle(self, name: str) -> None:
        """
        Для переключения вкладки в браузере.
        """
        self.driver.switch_to.window(name)

    def scroll_page_to_element(self, element: Component) -> None:
        self.driver.execute_script(
            'return arguments[0].scrollIntoView(true);',
            element,
        )

    def scroll_page_to_locator(
            self,
            locator: Locator,
    ) -> None:
        """
        Для скролла до заданного элемента на странице
        """
        element = self.driver_wait.until(
            method=EC.visibility_of_element_located(locator),
            message=f'Can\'t find element by locator {locator}',
        )
        self.scroll_page_to_element(element=element)

    def mouseover_to_element(self, element: Component) -> None:
        """
        Для наведения курсора до заданного элемента на странице
        """
        self.action_chains.move_to_element(element).perform()
