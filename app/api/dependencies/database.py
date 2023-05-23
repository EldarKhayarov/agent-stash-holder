from typing import Callable, Type

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from starlette.requests import Request

from app.db.repositories.base import BaseRepository


async def get_db_session(
    request: Request,
) -> AsyncSession:
    # Зависимость, возвращающая SQLAlchemy сессию.
    async with request.app.state.db_session() as session:
        yield session


def get_repository(
    repository_class: Type[BaseRepository],
) -> Callable[[AsyncSession], BaseRepository]:
    def _get_repo(
        conn: AsyncSession = Depends(get_db_session),
    ) -> BaseRepository:
        return repository_class(conn)

    return _get_repo
