import tempfile

import pytest
from typer.testing import CliRunner

from uv_python_project_template.main import app, fibonacci


runner = CliRunner()


@pytest.mark.parametrize(
    ("n", "nth_number"),
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (19, 4181),
        (200, 280571172992510140037611932413038677189525),
    ],
)
def test_fibonacci(n: int, nth_number: int) -> None:
    assert fibonacci(n) == nth_number


@pytest.mark.parametrize("args", [["1"], ["100"], ["--log-level", "debug", "1"]])
def test_main_success(args: list[str]) -> None:
    result = runner.invoke(app, args)
    assert result.exit_code == 0


@pytest.mark.parametrize("args", [["asd"], ["-1"], [""], [], ["--log-level", "invalid", "1"]])
def test_main_failure(args: list[str]) -> None:
    result = runner.invoke(app, args)
    assert result.exit_code == 2


def test_main_log_file() -> None:
    with tempfile.NamedTemporaryFile() as temp_file:
        result = runner.invoke(app, ["--log-file-path", temp_file.name, "1"])
        assert result.exit_code == 0
        assert temp_file.read()
