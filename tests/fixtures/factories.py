import pytest
from faker import Factory


@pytest.fixture(scope='session')
def fake():
    return Factory.create()
