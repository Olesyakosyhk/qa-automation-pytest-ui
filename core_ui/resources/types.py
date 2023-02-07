from typing import Literal, NewType


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
