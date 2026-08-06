import sys
from collections.abc import Callable

import pytest
import uvicorn

from neetcode_dashboard.__main__ import main


def test_cli_runs_validated_loopback_factory(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    invocation: dict[str, object] = {}

    def fake_run(application: str, **options: object) -> None:
        invocation["application"] = application
        invocation.update(options)

    monkeypatch.setattr(uvicorn, "run", fake_run)
    monkeypatch.setattr(
        sys,
        "argv",
        ["neetcode-dashboard", "--host", "localhost", "--port", "8123"],
    )

    main()

    assert invocation == {
        "application": "neetcode_dashboard.app:create_app",
        "factory": True,
        "host": "localhost",
        "port": 8_123,
        "log_level": "info",
    }


def test_cli_rejects_public_bind_address(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    called: list[bool] = []

    def fail_if_called(*_args: object, **_kwargs: object) -> None:
        called.append(True)

    replacement: Callable[..., None] = fail_if_called
    monkeypatch.setattr(uvicorn, "run", replacement)
    monkeypatch.setattr(
        sys,
        "argv",
        ["neetcode-dashboard", "--host", "0.0.0.0", "--port", "8123"],
    )

    with pytest.raises(SystemExit) as error:
        main()

    assert error.value.code == 2
    assert "0.0.0.0" in capsys.readouterr().err
    assert called == []


def test_cli_uses_environment_when_flags_are_omitted(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    invocation: dict[str, object] = {}

    def fake_run(application: str, **options: object) -> None:
        invocation["application"] = application
        invocation.update(options)

    monkeypatch.setattr(uvicorn, "run", fake_run)
    monkeypatch.setenv("NEETCODE_HOST", "localhost")
    monkeypatch.setenv("NEETCODE_PORT", "8124")
    monkeypatch.setattr(sys, "argv", ["neetcode-dashboard"])

    main()

    assert invocation["host"] == "localhost"
    assert invocation["port"] == 8_124
