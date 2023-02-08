from selenium.webdriver.remote.webdriver import WebDriver


__all__ = [
    'PageURL',
]


class PageURL:
    driver: WebDriver
    base_url: str
    page_url: str

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
