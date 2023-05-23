from app.models.domains.rwmodel import RWModel
from app.models.common import DateTimeModelMixin


class StashRequest(DateTimeModelMixin, RWModel):
    agent_id: str

