from __future__ import annotations

import argparse
from typing import Literal, TypedDict, cast

import uvicorn
from pydantic import ValidationError

from neetcode_dashboard.app import create_app
from neetcode_dashboard.config import Settings


class _SettingsOverrides(TypedDict, total=False):
    host: Literal["127.0.0.1", "localhost"]
    port: int


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the local NeetCode 500 Foundation dashboard")
    parser.add_argument("--host", default=None, help="127.0.0.1 or localhost only")
    parser.add_argument("--port", default=None, type=int, help="local TCP port")
    arguments = parser.parse_args()
    overrides = _SettingsOverrides()
    if arguments.host is not None:
        overrides["host"] = cast(Literal["127.0.0.1", "localhost"], arguments.host)
    if arguments.port is not None:
        overrides["port"] = cast(int, arguments.port)
    try:
        settings = Settings(**overrides)
    except ValidationError as error:
        parser.error(str(error))

    uvicorn.run(
        create_app(settings),
        host=settings.host,
        port=settings.port,
        log_level="info",
    )


if __name__ == "__main__":
    main()
