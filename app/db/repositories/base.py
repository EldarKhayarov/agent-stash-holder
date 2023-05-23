from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    """
    Классы для взаимодействия с БД.
    """

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    @property
    def session(self) -> AsyncSession:
        return self._session
