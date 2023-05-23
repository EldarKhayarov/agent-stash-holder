import datetime
from typing import Any, Sequence

from sqlalchemy import insert, select
from sqlalchemy.sql import text, func
from sqlalchemy.engine import Result, Row

from app.db.repositories.base import BaseRepository
from app.db.tables.stash import StashRequestTable


class StashRequestRepository(BaseRepository):
    async def insert_stash(self, *, agent_ids: list[str]) -> Result[Any]:
        """
        Создание отметок о запросах.
        :param agent_ids:
        :return:
        """
        agent_ids = set(agent_ids)
        new_items = [{"agent_id": agent_id} for agent_id in agent_ids]

        added_items = await self.session.execute(
            insert(StashRequestTable).returning(
                StashRequestTable.agent_id, StashRequestTable.created_at
            ),
            new_items,
        )
        await self.session.commit()

        return added_items

    async def get_stashes_in_period(
        self, agent_ids: list[str], period: int
    ) -> Sequence[Row]:
        """
        Получение списка отметок за заданный период в секундах.
        :param agent_ids:
        :param period:
        :return:
        """
        stashes_in_period = await self.session.execute(
            select(StashRequestTable.agent_id, StashRequestTable.created_at).where(
                StashRequestTable.created_at
                >= func.now() - datetime.timedelta(seconds=period),
                StashRequestTable.agent_id.in_(agent_ids),
            )
        )
        return stashes_in_period.all()

    async def get_agent_list(self) -> Result[Any]:
        """
        Получение списка ID агентов.
        :return:
        """
        agent_list = await self.session.execute(
            text("SELECT DISTINCT ON (agent_id) agent_id FROM stash_request")
        )
        return agent_list
