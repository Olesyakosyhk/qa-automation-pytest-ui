from typing import Literal, NewType


__all__ = [
    'LocatorType',
    'Locator',
]

LocatorType = NewType(
    'LocatorType',
    Literal[
        'id',
        'link text',
        'xpath',
        'partial link text',
        'name',
        'tag name',
        'class name',
        'css selector',
    ],
)

Locator = NewType(
    'Locator',
    tuple[LocatorType, str],
)
