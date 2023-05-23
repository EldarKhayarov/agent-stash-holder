import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.tables.base import BaseTable


class StashRequestTable(BaseTable):
    __tablename__ = "stash_request"

    agent_id: Mapped[str] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        primary_key=True, server_default=func.now()
    )
