from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from core import settings

__all__ = [
    'PageURL',
]


class PageURL:
    def __init__(
            self,
            driver: WebDriver,
            path: str | None = None,
    ) -> None:
        self.driver = driver
        self.driver_wait = WebDriverWait(
            driver=self.driver,
            timeout=settings.WEB_DRIVER_WAIT_TIMEOUT,
        )

        self.base_url = settings.BASE_URL
        self.page_url = f'{self.base_url}{path}'

    def get_current_url(self) -> str:
        """
        Для определения текущего УРЛ.
        """
        return self.driver.current_url

    def go_to_page_by_url(self) -> None:
        self.driver.get(self.page_url)

    def check_url(self) -> bool:
        """
        Проверка url страницы
        """
        return self.get_current_url() == self.page_url
