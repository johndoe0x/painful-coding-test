from __future__ import annotations

import fcntl
import os
from dataclasses import dataclass
from pathlib import Path


class DatabaseLockError(RuntimeError):
    """Raised when another process owns the dashboard database lock."""


@dataclass(slots=True)
class DatabaseRuntimeLock:
    _descriptor: int
    path: Path
    _released: bool = False

    def __enter__(self) -> DatabaseRuntimeLock:
        return self

    def __exit__(self, *_error: object) -> None:
        self.release()

    def release(self) -> None:
        if self._released:
            return
        try:
            fcntl.flock(self._descriptor, fcntl.LOCK_UN)
        finally:
            os.close(self._descriptor)
            self._released = True


def acquire_database_runtime_lock(database_path: Path) -> DatabaseRuntimeLock:
    database = database_path.expanduser().resolve()
    database.parent.mkdir(parents=True, exist_ok=True)
    lock_path = database.parent / f".{database.name}.runtime.lock"
    descriptor = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o600)
    try:
        fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError as error:
        os.close(descriptor)
        raise DatabaseLockError("dashboard database is locked by another process") from error
    return DatabaseRuntimeLock(descriptor, lock_path)
