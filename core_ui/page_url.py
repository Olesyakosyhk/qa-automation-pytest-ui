from core_ui.url import URL


class PageURL(URL):

    def get_current_url(self) -> str:
        """
        Для определения текущего УРЛ.
        """
        return self.driver.current_url

    def go_to_page(self) -> None:
        self.driver.get(self.page_url)

    def check_url(self) -> bool:
        """
        Проверка url страницы
        """
        return self.get_current_url() == self.page_url
