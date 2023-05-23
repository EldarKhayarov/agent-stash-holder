import pytest
from httpx import AsyncClient

from app.tests.utils import HOST, PORT


@pytest.fixture
async def http_client(application):
    """
    Фикстура для получения HTTP клиента.
    :param application:
    :return:
    """
    async with AsyncClient(
        app=application, base_url="http://{host}:{port}".format(host=HOST, port=PORT)
    ) as client:
        yield client
