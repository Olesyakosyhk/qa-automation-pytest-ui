from selenium.webdriver.remote.webdriver import WebDriver


__all__ = [
    'Frame',
]


class Frame:
    def __init__(
            self,
            driver: WebDriver,
    ) -> None:
        self.driver = driver

    def switch_to(self, frame_name) -> None:
        """
        Для переключения фрейм.
        """
        self.driver.switch_to.frame(frame_name)
