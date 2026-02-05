"""Utilities."""

import enum
from datetime import timedelta
from pathlib import Path
from typing import Any

from loguru import logger
from tabulate import tabulate


class LogLevel(enum.StrEnum):
    """Log level."""

    CRITICAL = "critical"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"
    DEBUG = "debug"


def is_non_empty_file(file_path: str | Path) -> bool:
    """Return `True` if `file_path` points to a non-empty file."""
    file_path = Path(file_path)
    return file_path.is_file() and file_path.stat().st_size > 0


def get_time_elapsed_string(elapsed_time: float | timedelta) -> str:
    """Given `elapsed_time`, construct a human-readable string of how much time has elapsed."""
    td = elapsed_time if isinstance(elapsed_time, timedelta) else timedelta(seconds=elapsed_time)
    days = int(td.days)
    tot_seconds = td.seconds
    hours = int(tot_seconds / 3600)
    rest_seconds = tot_seconds % 3600
    minutes = int(rest_seconds / 60)
    seconds = int(rest_seconds % 60)

    # Decide how many units to include.
    if days:
        output_string = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    elif hours:
        output_string = f"{hours} hours, {minutes} minutes, {seconds} seconds"
    else:
        output_string = f"{minutes} minutes, {seconds} seconds"

    # Make singular if necessary.
    if days == 1:
        output_string = output_string.replace("days", "day")
    if hours == 1:
        output_string = output_string.replace("hours", "hour")
    if minutes == 1:
        output_string = output_string.replace("minutes", "minute")
    if seconds == 1:
        output_string = output_string.replace("seconds", "second")

    return output_string


def get_ordinal_suffix(integer: int) -> str:
    """Given an integer, return the correct ordinal suffix, e.g., 'st' (for 'first') if the integer is 1."""
    # All numbers ending in 10, 11, ..., 20 have the suffix 'th'.
    if 10 <= abs(integer) % 100 <= 20:  # noqa: PLR2004
        return "th"
    # All other numbers have a suffix based on the last digit.
    return {1: "st", 2: "nd", 3: "rd"}.get(abs(integer) % 10, "th")


def pretty_log_dict(arguments: dict[str, Any], header: tuple[str, str] = ("key", "value")) -> None:
    """Log the keys and values of the input dictionary as a nicely-formatted table."""
    table = [list(header)]
    for k, v in arguments.items():
        table.append([k, v])
    for row in tabulate(table, headers="firstrow").splitlines():
        logger.info(row)
