import logging

import pytest

from sqlalchemy.ext.asyncio import create_async_engine

from app.db.tables.base import BaseTable
from app.core.config import get_app_settings


@pytest.fixture(scope="session", autouse=True)
async def recreate_database_tables():
    """
    Фикстура для пересоздания таблиц после предыдущих тестов.
    :return:
    """
    settings = get_app_settings()
    engine = create_async_engine(
        settings.database_dsn,
        pool_size=settings.min_connection_count,
        max_overflow=settings.max_connection_count - settings.min_connection_count,
    )

    logging.info("Recreating tables...")
    async with engine.begin() as conn:
        await conn.run_sync(BaseTable.metadata.drop_all)
        await conn.run_sync(BaseTable.metadata.create_all)

    logging.info("Tables recreated.")
