from typing import NewType, Literal

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
