import logging
import sys
from typing import Any, Dict

from loguru import logger
from pydantic import PostgresDsn, DirectoryPath

from app.core.logging import InterceptHandler
from app.core.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    """
    Класс для хранения констант конфига и удобного к ним доступа из разных участков кода.
    """

    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "Agent Stash Holder [FastAPI + Python 3.11]"
    version: str = "0.0.1"

    database_dsn: PostgresDsn
    max_connection_count: int = 10
    min_connection_count: int = 10

    api_prefix: str = "/api"

    allowed_hosts: list[str] = ["*"]
    cors_allow_credentials: bool = True
    cors_allow_methods: list[str] = ["*"]
    cors_allow_headers: list[str] = ["*"]

    static_files_dir: DirectoryPath
    static_files_url_path: str = ""

    logging_level: int = logging.INFO
    loggers: tuple[str, str] = ("uvicorn.asgi", "gunicorn.access")

    class Config:
        validate_assignment = True

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }

    def configure_logging(self) -> None:
        # Связывание стандартных логеров с логерами loguru.
        logging.getLogger().handlers = [InterceptHandler()]
        for logger_name in self.loggers:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler(level=self.logging_level)]

        logger.configure(handlers=[{"sink": sys.stderr, "level": self.logging_level}])
