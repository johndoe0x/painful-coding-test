from __future__ import annotations

from .collections_io_exceptions import EXERCISES as COLLECTIONS_IO_EXCEPTIONS
from .functions_conditionals_loops import EXERCISES as FUNCTIONS_CONDITIONALS_LOOPS
from .intro_variables_math import EXERCISES as INTRO_VARIABLES_MATH
from .model import Exercise
from .strings_lists import EXERCISES as STRINGS_LISTS


EXERCISES: dict[str, list[Exercise]] = {}
for _catalog in (
    INTRO_VARIABLES_MATH,
    FUNCTIONS_CONDITIONALS_LOOPS,
    STRINGS_LISTS,
    COLLECTIONS_IO_EXCEPTIONS,
):
    overlap = EXERCISES.keys() & _catalog.keys()
    if overlap:
        raise RuntimeError(f"duplicate exercise seeds: {sorted(overlap)}")
    EXERCISES.update(_catalog)


__all__ = ["EXERCISES", "Exercise"]
