from selenium.webdriver.remote.webdriver import WebDriver


__all__ = [
    'Alert',
]


class Alert:

    def __init__(
            self,
            driver: WebDriver,
    ) -> None:
        self.driver = driver

    def accept(self) -> None:
        """
        Принять alert.
        """
        self.driver.switch_to.alert.accept()

    def dismiss(self) -> None:
        """
        Отклонить alert.
        """
        self.driver.switch_to.alert.dismiss()

    def get_text(self) -> None:
        """
        Получение сообщения из всплывающего окна alert.
        """
        self.driver.switch_to.alert.text()
