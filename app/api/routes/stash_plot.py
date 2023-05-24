import datetime

import numpy as np
from fastapi import APIRouter, Depends
from fastapi.responses import Response

from app.api.queries import get_agent_id_query
from app.api.dependencies.database import get_repository
from app.db.repositories.stash import StashRequestRepository
from app.services.plot_generator import generate_time_scatter_plot


router = APIRouter()


@router.api_route("", methods=["GET", "POST"])
async def generate_stash_plot(
    period: int,
    agent_ids: list[str] = get_agent_id_query(),
    stash_repo: StashRequestRepository = Depends(
        get_repository(StashRequestRepository)
    ),
):
    """
    Генерация графика запросов во времени.

    :param period:
    :param agent_ids:
    :param stash_repo:
    :return:
    """
    stashes = await stash_repo.get_stashes_in_period(agent_ids=agent_ids, period=period)

    agents_array = np.zeros(len(stashes), dtype="U16")
    dtime_array = np.zeros(len(stashes), dtype="datetime64[s]")
    last_timestamp = datetime.datetime.now()

    for idx, stash in enumerate(stashes):
        agents_array[idx] = stash.agent_id
        dtime_array[idx] = stash.created_at

    plot_buffer = generate_time_scatter_plot(
        agents_array, dtime_array, last_timestamp, period
    )
    return Response(plot_buffer.getvalue(), media_type="image/png")
