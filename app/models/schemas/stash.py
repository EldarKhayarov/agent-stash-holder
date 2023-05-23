from app.models.schemas.rwschema import RWSchema
from app.models.domains.stash import StashRequest


class StashRequestOut(RWSchema, StashRequest):
    pass
