from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from core import settings


class URL:

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
