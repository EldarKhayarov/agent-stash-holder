from typing import Any

from fastapi import Query
from pydantic.fields import Undefined


def get_agent_id_query(
    default: Any = Undefined,
    alias: str = "ids",
    regex: str = r"id\d+$",
    example: str = "id123",
):
    """
    Фабрика объектов query для agent_id.

    Необходима для применения идентичных конфигураций Query в разных участках кода.
    :param default:
    :param alias:
    :param regex:
    :param example:
    :return:
    """
    return Query(default, alias=alias, regex=regex, example=example)
