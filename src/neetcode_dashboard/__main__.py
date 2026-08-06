from __future__ import annotations

import argparse

import uvicorn
from pydantic import ValidationError

from neetcode_dashboard.config import Settings


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the local NeetCode 500 Foundation dashboard")
    parser.add_argument("--host", default=None, help="127.0.0.1 or localhost only")
    parser.add_argument("--port", default=None, type=int, help="local TCP port")
    arguments = parser.parse_args()
    try:
        environment = Settings()
        settings = Settings(
            host=arguments.host if arguments.host is not None else environment.host,
            port=arguments.port if arguments.port is not None else environment.port,
        )
    except ValidationError as error:
        parser.error(str(error))

    uvicorn.run(
        "neetcode_dashboard.app:create_app",
        factory=True,
        host=settings.host,
        port=settings.port,
        log_level="info",
    )


if __name__ == "__main__":
    main()
