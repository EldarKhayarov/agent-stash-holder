import datetime
import dateutil.parser

import pytest
from fastapi import status

from app.tests.fixtures.database import recreate_database_tables
from app.tests.fixtures.common import anyio_backend
from app.tests.fixtures.application import application
from app.tests.fixtures.clients import http_client


@pytest.mark.anyio
async def test_stashing(application, http_client):
    agent_ids = ["id1", "id2"]
    time_before_request = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc
    )
    response = await http_client.get("/stash", params={"ids": agent_ids})
    response_body = response.json()
    time_after_request = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.headers["content-type"] == "application/json"
    assert {agent_item["agentId"] for agent_item in response_body} == set(agent_ids)
    assert (
        time_before_request
        <= dateutil.parser.isoparse(response_body[0]["createdAt"]).astimezone(
            tz=datetime.timezone.utc
        )
        <= time_after_request
    )

    response = await http_client.post("/stash", params={"ids": "id1,id2"})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    response = await http_client.get("/stash", params={"ids": ["idd1"]})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    response = await http_client.post("/stash", params={"ids": ["id-2"]})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.anyio
async def test_agent_ids(application, http_client):
    agent_ids = ["id1", "id2", "id3"]

    response = await http_client.get("/stash", params={"ids": agent_ids[0]})
    assert response.status_code == status.HTTP_201_CREATED

    response = await http_client.get("/stash", params={"ids": agent_ids[1:]})
    assert response.status_code == status.HTTP_201_CREATED

    response = await http_client.get("/agent/all")
    assert response.json() == agent_ids
