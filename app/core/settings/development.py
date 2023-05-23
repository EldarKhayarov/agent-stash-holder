import logging

from app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True

    title: str = "DEV: Agent Stash Holder [FastAPI + Python 3.11]"

    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = ".env"
