import datetime

from pydantic import BaseModel, validator


class DateTimeModelMixin(BaseModel):
    created_at: datetime.datetime = None

    @validator("created_at", pre=True)
    def default_datetime(
        cls,
        value: datetime.datetime,
    ) -> datetime.datetime:
        return value or datetime.datetime.utcnow()
