from selenium.webdriver.common.by import By

from core_ui.components import Component
from core_ui.page import BasePage


__all__ = [
    'DynamicTablePage',
]


class DynamicTablePage(BasePage):
    """
    Получение локатора из динамической таблицы.

    Page URL:
        http://uitestingplayground.com/dynamictable
    """
    COLUMN_COUNT = 6
    ROW_COUNT = 6
    BROWSER_NAME = 'Chrome'
    CPU = 'CPU'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.value_chrome_cpu = Component(
            driver=self.driver,
            locator_type=By.CSS_SELECTOR,
            locator_path='[class="bg-warning"]',
        )

    def _build_component_value_table_chrome_cpu(
            self,
            x_param: int,
            y_param: int,
    ) -> Component:
        return Component(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path=f'//div[3]/div[{y_param}]/span[{x_param}]',
        )

    def _build_cpu_name(
            self,
            x_param: int,
    ) -> Component:
        return Component(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path=f'//*[@role="table"]/div[@role="rowgroup"]/div/span[{x_param}]',
        )

    def _build_browser_name(
            self,
            y_param: int,
    ) -> Component:
        return Component(
            driver=self.driver,
            locator_type=By.XPATH,
            locator_path=f'//div[3]/div[{y_param}]/span[1]',
        )

    def get_locator_cpu(self) -> int:
        """
        Ищем столбец с именем CPU.
        """
        for x_param in range(1, self.COLUMN_COUNT):
            cpu_name_component = self._build_cpu_name(x_param=x_param)
            if cpu_name_component.check_text(text=self.CPU):
                return x_param

    def get_locator_chrome_name(self) -> int:
        for y_param in range(1, self.ROW_COUNT):
            browser_name_component = self._build_browser_name(y_param=y_param)
            if browser_name_component.check_text(text=self.BROWSER_NAME):
                return y_param

    def get_locator_chrome_cpu(self) -> Component:
        x_param = self.get_locator_cpu()
        y_param = self.get_locator_chrome_name()

        value_table_cpu = self._build_component_value_table_chrome_cpu(
            x_param=x_param,
            y_param=y_param,
        )
        return value_table_cpu

    def check_value_chrome_cpu(
            self,
            value_table_cpu,
    ) -> bool:
        return value_table_cpu.element.text in self.value_chrome_cpu.element.text
