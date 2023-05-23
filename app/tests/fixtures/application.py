import pytest

from app.core.events import create_start_app_handler, create_stop_app_handler
from app.main import get_application
from app.core.config import get_app_settings


@pytest.fixture
async def application():
    """
    Фикстура для получения объекта приложения в каждом тесткейсе.
    :return:
    """
    settings = get_app_settings()
    application = get_application()
    await create_start_app_handler(application, settings)()

    yield application

    await create_stop_app_handler(application)()
