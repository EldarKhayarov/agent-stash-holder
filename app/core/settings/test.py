import logging

from app.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    debug: bool = True

    title: str = "TEST: Agent Stash Holder [FastAPI + Python 3.11]"

    max_connection_count: int = 5
    min_connection_count: int = 5

    logging_level: int = logging.DEBUG
