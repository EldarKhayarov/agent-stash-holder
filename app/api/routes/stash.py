from fastapi import APIRouter, Depends, status
from pydantic import constr

from app.api.queries import get_agent_id_query
from app.api.dependencies.database import get_repository
from app.db.repositories.stash import StashRequestRepository
from app.models.schemas.stash import StashRequestOut


router = APIRouter()


@router.api_route(
    "/stash",
    methods=["GET", "POST"],
    response_model=list[StashRequestOut],
    status_code=status.HTTP_201_CREATED,
)
async def stash(
    agent_ids: list[str] = get_agent_id_query(),
    stash_repo: StashRequestRepository = Depends(
        get_repository(StashRequestRepository)
    ),
):
    added_items = await stash_repo.insert_stash(agent_ids=agent_ids)
    return [StashRequestOut.from_orm(added_item) for added_item in added_items]


@router.get(
    "/agent/all",
    response_model=list[constr(regex=r"^id\d+$")],
)
async def get_agent_all(
    stash_repo: StashRequestRepository = Depends(
        get_repository(StashRequestRepository)
    ),
):
    agents = await stash_repo.get_agent_list()
    return [agent[0] for agent in agents]
