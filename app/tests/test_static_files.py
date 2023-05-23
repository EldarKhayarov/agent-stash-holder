import os
import asyncio

import pytest
from fastapi import status

from app.tests.fixtures.database import recreate_database_tables
from app.tests.fixtures.common import anyio_backend
from app.tests.fixtures.clients import http_client
from app.tests.fixtures.application import application
from app.tests.utils import (
    PROJECT_ROOT,
    NOT_FOUND_MESSAGE,
    read_file_coroutine,
    generate_unreal_file_path,
)


@pytest.mark.anyio
async def test_get_static_files(application, http_client):
    static_root = os.path.join(PROJECT_ROOT, "tests", "static")
    file_index_html, file_text, file_image = await asyncio.gather(
        read_file_coroutine(os.path.join(static_root, "index.html"), mode="rb"),
        read_file_coroutine(os.path.join(static_root, "txts", "top text"), mode="rb"),
        read_file_coroutine(os.path.join(static_root, "imgs", "travis.jpg"), mode="rb"),
    )

    response = await http_client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert response.content == file_index_html

    response = await http_client.get("/txts/top text")
    assert response.status_code == status.HTTP_200_OK
    assert response.headers["content-type"] == "text/plain; charset=utf-8"
    assert response.content == file_text

    response = await http_client.get("/imgs/travis.jpg")
    assert response.status_code == status.HTTP_200_OK
    assert response.headers["content-type"] == "image/jpeg"
    assert response.content == file_image

    response = await http_client.get(generate_unreal_file_path())
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == NOT_FOUND_MESSAGE
