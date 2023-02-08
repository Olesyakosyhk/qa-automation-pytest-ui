from core_ui.components.component import Component


__all__ = [
    'Input',
]


class Input(Component):
    def set_text(self, text: str) -> None:
        """
        Ввести текст.
        """
        self.element.send_keys(text)

    def delete_text(self, text: str) -> None:
        """
        Удаление текста из поля.
        """
        self.element.clear()
