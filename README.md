# `uv` Python Project Template

[![Python 3.14](https://img.shields.io/badge/python-3.14-blue.svg)](https://docs.python.org/3/whatsnew/3.14.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-9400d3.svg)](https://opensource.org/licenses/MIT)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Mypy](https://img.shields.io/badge/type%20checked-mypy-039dfc)](https://github.com/python/mypy)
[![Pytest](https://img.shields.io/static/v1?label=‎&message=Pytest&logo=Pytest&color=b647c4&logoColor=white)](https://docs.pytest.org)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Deploy to Cloud Run](https://github.com/h-holm/uv-python-project-template/workflows/Deploy%20to%20Cloud%20Run/badge.svg)](https://github.com/h-holm/uv-python-project-template/actions/workflows/deploy-to-cloud-run.yaml)
[![CodeQL](https://github.com/h-holm/uv-python-project-template/workflows/CodeQL%20Analysis/badge.svg)](https://github.com/h-holm/uv-python-project-template/actions/workflows/codeql-analysis.yaml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/h-holm/uv-python-project-template/main.svg)](https://results.pre-commit.ci/latest/github/h-holm/uv-python-project-template/main)

A template repo that enables quickly setting up an end-to-end CI/CD pipeline that tests and deploys a containerized
Python application. The placeholder Python logic computes a Fibonacci number.

## Features ✅

* Environment management and dependency resolution via [uv](https://github.com/astral-sh/uv)
* Primary dependencies and tooling configuration in the [PEP](https://peps.python.org/pep-0621)-recommended
[pyproject.toml](./pyproject.toml) file
* (Sub-)dependency locking in [`uv.lock`](./uv.lock) file
* Linting and formatting using [ruff](https://github.com/astral-sh/ruff)
* Static type checking using [mypy](https://github.com/python/mypy)
* [pytest](https://docs.pytest.org) for unit tests with [coverage](https://coverage.readthedocs.io/en/latest)-based
reporting
* [./src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout) to separate application
logic from tests and project metadata
* Sane logging configured in a single [logging.conf](./src/python_project_template/logging.conf) file
* Optional quality-of-life add-ons:
  * [pre-commit](https://github.com/pre-commit/pre-commit) hooks via the `pre` dependency group
  * (further) enforcing of uniform formatting via an [.editorconfig](./.editorconfig)
  * recommended [VS Code](https://code.visualstudio.com) settings and extensions through a [.vscode](./.vscode)
  subdirectory

### [GitHub Actions](./.github/workflows/) [CI/CD](https://www.redhat.com/en/topics/devops/what-is-ci-cd)

On any pull request, target a `stg` staging environment and:

* run [ruff](https://github.com/astral-sh/ruff)-based linting and formatting,
[mypy](https://github.com/python/mypy)-based static type checking, and [pytest](https://docs.pytest.org)-based unit
testing;
* perform a [CodeQL](https://codeql.github.com) vulnerability scan;
* build and push a well-labeled container image to a
[Google Cloud Artifact Registry](https://cloud.google.com/artifact-registry/docs);
* execute an integration test on [Google Cloud Run](https://cloud.google.com/run?hl=en) that runs the application
logic end-to-end.

On a commit/tag being merged/pushed (in)to the `main` branch, target a `prd` production environment and:

* perform the same steps as above;
* deploy a Cloud Run job;
* promote the now-vetted container image by adding tags such as `latest`, `main` and the [SemVer](https://semver.org)
tag (if any).

## Requirements

Install [`uv`](https://docs.astral.sh/uv/getting-started/installation).

## Development

### Running the Code

```shell
uv run src/uv_python_project_template/main.py --help  # Display help message and explain available flags.
uv run src/uv_python_project_template/main.py 123     # Compute the 123rd Fibonacci number.
```

### Unit Testing

```shell
uv run --group test pytest                            # Run all `./tests` unit tests and compute a coverage report.
uv run --group test pytest --verbose                  # Same as above, but provide additional information.
uv run --group test pytest tests/test_utils.py        # Execute (only) the `tests/test_utils.py` unit tests.
uv run --group test pytest --cov-report=xml           # Execute unit tests and write coverage report to `coverage.xml`.
uv run --group test pytest --pdb                      # Execute unit tests in debug mode.
```

### Linting

```shell
uv run --group lint ruff check                        # Lint files.
uv run --group lint ruff check --fix                  # Lint files and fix any fixable errors.
uv run --group lint ruff check --watch                # Lint files and re-lint on change.
uv run --group lint ruff check ${PATH}                # Lint file(s) at ${PATH}.
```

### Formatting

```shell
uv run --group lint ruff format --check               # Check if files adhere to `ruff` formatting rules.
uv run --group lint ruff format                       # Format files.
uv run --group lint ruff format ${PATH}               # Format file(s) at ${PATH}.
```

### Type Checking

```shell
uv run --group lint mypy .                            # Run type checking.
uv run --group lint mypy ${PATH}                      # Format file(s) at ${PATH}.
```

### Optional [`pre-commit`](https://github.com/pre-commit/pre-commit) Hooks

The optional `pre-commit` hooks ensure that the linting, formatting and type checking steps described above all pass
before a commit is created. The hooks can be set up and used as follows:

```shell
uv run --group pre pre-commit install                 # Set up `pre-commit` hooks.
uv run --group pre pre-commit                         # Run `pre-commit` hooks.
```

### Upgrading Dependencies

```shell
uv lock --upgrade                                     # Upgrade all dependencies that can be upgraded.
uv lock --upgrade-package ${PACKAGE_NAME}             # Upgrade a specific dependency.
```

Commit the updated [uv.lock](uv.lock) file to version control.

### Bumping the Version

Bump the [SemVer](https://semver.org) version in the `project.version` attribute in the
[pyproject.toml](pyproject.toml) configuration. Then, commit the updated config to version control before creating a
`git` tag. Ensure the tag has the same name as the (now bumped) version:

```shell
git tag -a $(uv version --short) -m 'Descriptive tag message'
```

## License

See [LICENSE](LICENSE).
