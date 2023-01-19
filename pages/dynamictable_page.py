from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


__all__ = [
    'DynamicTablePage',
]


class DynamicTablePage(BasePage):
    """
    Получение локатора из динамической таблицы.

    Page URL:
        http://uitestingplayground.com/dynamictable
    """

    # Локаторы...
    # Таблица...
    TABLE_COLUMN_NAMES = (By.CSS_SELECTOR, '[role="table"]> div:nth-child(2)> div')
    CPU_NAME = (By.XPATH, '//*[@role="table"]/div[@role="rowgroup"]/div/span[{x_param}]')
    BROWSER_NAME = (By.XPATH, '//div[3]/div[{y_param}]/span[1]')
    COLUMN_IS_NAME = (By.CSS_SELECTOR, '[role="table"]> div:nth-child(2)')

    VALUE_TABLE_CHROME_CPU = (By.XPATH, '//div[3]/div[{y_param}]/span[{x_param}]')
    VALUE_CHROME_CPU = (By.CSS_SELECTOR, '[class="bg-warning"]')

    def _get_locator_by_param(self, locator: tuple, x_param: int, y_param: int,):
        return locator[0], locator[1].format(x_param=x_param, y_param=y_param)

    def _get_locator_by_x_param(
            self, locator: tuple, x_param: int):
        return locator[0], locator[1].format(x_param=x_param)

    def _get_locator_by_y_param(self, locator: tuple, y_param: int):
        return locator[0], locator[1].format(y_param=y_param)

    def get_locator_cpu(self) -> int:
        for x_param in range(1, 6):
            table_column_name = self.find_and_wait_element(self._get_locator_by_x_param(self.CPU_NAME, x_param))
            if table_column_name.text == 'CPU':
                return x_param

    def get_locator_chrome_name(self) -> int:
        for y_param in range(1, 6):
            browser_name = self.find_and_wait_element(self._get_locator_by_y_param(self.BROWSER_NAME, y_param))
            if browser_name.text == 'Chrome':
                return y_param

    def get_locator_chrome_cpu(self) -> WebElement:
        x_param = self.get_locator_cpu()
        y_param = self.get_locator_chrome_name()

        value_table_cpu = self.find_and_wait_element(
            self._get_locator_by_param(self.VALUE_TABLE_CHROME_CPU, x_param, y_param),
        )
        return value_table_cpu

    def check_value_chrome_cpu(self, value_table_cpu) -> bool:
        value_chrome_cpu = self.find_and_wait_element(self.VALUE_CHROME_CPU)
        return value_table_cpu.text in value_chrome_cpu.text
