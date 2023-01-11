import allure
import pytest

from pages import PlaygroundPage


class TestHiddenLayers:
    def test_hidden_layers_positive(
            self,
            playground_page: PlaygroundPage,
            go_to_hidden_layers_page,
    ):
        with allure.step('Нажать на зеленую кнопку'):
            playground_page.hidden_layers.click_green_btn()

        with pytest.raises(Exception) as exc_info:
            with allure.step('Повторить нажатие на зеленую кнопку'):
                playground_page.hidden_layers.click_green_btn()

        with allure.step(f'Проверка ответа | {exc_info.value.args[0]=}'):
            assert exc_info.value.args[0].startswith('element click intercepted:')
