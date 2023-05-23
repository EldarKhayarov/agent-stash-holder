from app.models.domains.rwmodel import RWModel


class RWSchema(RWModel):
    class Config(RWModel.Config):
        orm_mode = True
