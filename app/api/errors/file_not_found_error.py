from fastapi.openapi.constants import REF_PREFIX
from fastapi.openapi.utils import validation_error_response_definition
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


async def file_not_found_error_handler(
    _: Request,
    exc: ValidationError,
) -> JSONResponse:
    return JSONResponse(
        {"errors": exc.errors()},
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
    )


validation_error_response_definition["properties"] = {
    "errors": {
        "title": "Errors",
        "type": "array",
        "items": {"$ref": "{0}ValidationError".format(REF_PREFIX)},
    },
}
