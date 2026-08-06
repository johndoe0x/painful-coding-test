from __future__ import annotations

import argparse

import uvicorn
from pydantic import ValidationError

from neetcode_dashboard.config import Settings


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the local NeetCode 500 Foundation dashboard")
    parser.add_argument("--host", default="127.0.0.1", help="127.0.0.1 or localhost only")
    parser.add_argument("--port", default=51_115, type=int, help="local TCP port")
    arguments = parser.parse_args()
    try:
        settings = Settings(host=arguments.host, port=arguments.port)
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
