import pytest
from faker import Factory


__all__ = [
    'fake',
]


@pytest.fixture(scope='session')
def fake():
    return Factory.create('ru_RU')
