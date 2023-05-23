from fastapi import FastAPI
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)
from loguru import logger

from app.core.settings.app import AppSettings


async def make_db_async_session(app: FastAPI, settings: AppSettings) -> None:
    """
    Функция для создания сессии при запуске сервера.
    :param app:
    :param settings:
    :return:
    """
    logger.info("Connecting to PostgreSQL")

    engine = create_async_engine(
        settings.database_dsn,
        pool_size=settings.min_connection_count,
        max_overflow=settings.max_connection_count - settings.min_connection_count,
    )
    app.state.db_session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def close_db_connection(app: FastAPI) -> None:
    """
    Функция завершения сессии БД после завершения работы сервера.
    :param app:
    :return:
    """
    logger.info("Closing connection to database")

    app.state.db_session.close_all()

    logger.info("Connection closed")
