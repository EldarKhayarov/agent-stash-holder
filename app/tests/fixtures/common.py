import pytest


@pytest.fixture(scope="session")
def anyio_backend():
    """
    Конфигурация pytest.
    :return:
    """
    return "asyncio"
