from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from uv_python_project_template.utils.utils import (
    get_ordinal_suffix,
    get_time_elapsed_string,
    is_non_empty_file,
)


if TYPE_CHECKING:
    from datetime import timedelta


@pytest.mark.parametrize(
    ("file_path", "expected_output"),
    [
        ("non_existent_file", False),  # This file should not exist.
        (Path(__file__), True),  # This file itself is non-empty.
        (Path(__file__).parents[0] / "__init__.py", False),  # `__init__.py` should be empty.
    ],
)
def test_is_non_empty_file(file_path: str | Path, expected_output: bool) -> None:
    assert is_non_empty_file(file_path) == expected_output


@pytest.mark.parametrize(
    ("timestamp", "expected_output"),
    [
        (0, "0 minutes, 0 seconds"),
        (1, "0 minutes, 1 second"),
        (62, "1 minute, 2 seconds"),
        (60 * 60, "1 hour, 0 minutes, 0 seconds"),
        (60 * 60 * 24 + 123, "1 day, 0 hours, 2 minutes, 3 seconds"),
        (60 * 60 * 50 + 120, "2 days, 2 hours, 2 minutes, 0 seconds"),
    ],
)
def test_get_time_elapsed_string(timestamp: float | timedelta, expected_output: str) -> None:
    assert get_time_elapsed_string(timestamp) == expected_output


@pytest.mark.parametrize(
    ("integer", "expected_output"),
    [
        (0, "th"),
        (1, "st"),
        (2, "nd"),
        (3, "rd"),
    ]
    + [
        (-1, "st"),
        (-2, "nd"),
        (-3, "rd"),
    ]
    # All numbers between 4 and 20 have the suffix 'th'.
    + [(i, "th") for i in range(4, 21)]
    # All numbers between -20 and -4 have the suffix 'th'.
    + [(-i, "th") for i in range(4, 21)]
    + [
        (120, "th"),
        (121, "st"),
        (122, "nd"),
        (123, "rd"),
        (124, "th"),
        (-225, "th"),
        (1306, "th"),
    ],
)
def test_get_ordinal_suffix(integer: int, expected_output: str) -> None:
    assert get_ordinal_suffix(integer) == expected_output
