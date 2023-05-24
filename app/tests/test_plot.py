import pytest
from fastapi import status

from app.tests.fixtures.database import recreate_database_tables
from app.tests.fixtures.common import anyio_backend
from app.tests.fixtures.application import application
from app.tests.fixtures.clients import http_client


@pytest.mark.anyio
async def test_plot_generation(application, http_client):
    agent_ids = ["id1", "id2"]
    period_seconds = 60

    response = await http_client.get("/stash", params={"ids": agent_ids})
    assert response.status_code == status.HTTP_201_CREATED

    response = await http_client.get(
        "/plot", params={"ids": agent_ids, "period": period_seconds}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.headers["content-type"] == "image/png"

    response = await http_client.post(
        "/plot", params={"ids": agent_ids, "period": period_seconds}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.headers["content-type"] == "image/png"
