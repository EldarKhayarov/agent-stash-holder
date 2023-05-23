import os
import random
import string

import aiofiles


HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", "80")
PROJECT_ROOT = os.getenv("HOME", "/app")

NOT_FOUND_MESSAGE = {"errors": ["Not Found"]}


async def read_file_coroutine(file_path: str, **kwargs) -> bytes | str:
    async with aiofiles.open(file_path, **kwargs) as f:
        result = await f.read()
    return result


def generate_unreal_file_path(
    root: str = "", path_length: int = 10, get_absolute_path: bool = False
) -> str:
    """
    Создание пути к несуществующему файлу.
    :param root:
    :param path_length:
    :param get_absolute_path:
    :return:
    """
    path = _generate_random_char_sequence(path_length)

    while os.path.exists(
        os.path.join(root, _generate_random_char_sequence(path_length))
    ):
        path = _generate_random_char_sequence(path_length)

    if get_absolute_path:
        path = os.path.join(root, path)

    return path


def _generate_random_char_sequence(length: int) -> str:
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
    )
