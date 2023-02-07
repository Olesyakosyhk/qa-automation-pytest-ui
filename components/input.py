from components.component import Component


__all__ = [
    'Input',
]


class Input(Component):
    def set_text(self, text: str) -> None:
        """
        Ввести текст.
        """
        self.element.send_keys(text)
