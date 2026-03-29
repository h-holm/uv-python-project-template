# `uv` Python Project Template

[![Python 3.14](https://img.shields.io/badge/python-3.14-blue.svg)](https://docs.python.org/3/whatsnew/3.14.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-9400d3.svg)](https://opensource.org/licenses/MIT)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![ty](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![Pytest](https://img.shields.io/static/v1?label=‎&message=Pytest&logo=Pytest&color=b647c4&logoColor=white)](https://docs.pytest.org)
[![prek](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)
[![Deploy to Cloud Run](https://github.com/h-holm/uv-python-project-template/workflows/Deploy%20to%20Cloud%20Run/badge.svg)](https://github.com/h-holm/uv-python-project-template/actions/workflows/deploy-to-cloud-run.yaml)
[![CodeQL](https://github.com/h-holm/uv-python-project-template/workflows/CodeQL%20Analysis/badge.svg)](https://github.com/h-holm/uv-python-project-template/actions/workflows/codeql-analysis.yaml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/h-holm/uv-python-project-template/main.svg)](https://results.pre-commit.ci/latest/github/h-holm/uv-python-project-template/main)

Template repo that enables quick set-up of an end-to-end CI/CD pipeline that (1) tests and (2) deploys a containerized
Python application. The placeholder Python logic computes a Fibonacci number.

## Features ✅

* Environment management and dependency resolution via [uv](https://github.com/astral-sh/uv)
* [pyproject.toml](./pyproject.toml) for dependencies and tooling configuration
* Dependency locking via [uv.lock](./uv.lock)
* [ruff](https://github.com/astral-sh/ruff)-based linting and formatting
* Type checking using [ty](https://github.com/astral-sh/ty)
* [pytest](https://docs.pytest.org)-powered unit tests with [coverage](https://coverage.readthedocs.io/en/latest)-based
reporting
* Structured logging via [Loguru](https://github.com/Delgan/loguru)
* [./src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout) to separate application
logic from tests and other peripherals
* Optional quality-of-life add-ons:
  * automated dependency upgrading and vulnerability scans via [Dependabot](https://github.com/dependabot)
  * [prek](https://github.com/j178/prek)-based pre-commit hooks
  * (further) enforcing of uniform formatting via an [.editorconfig](./.editorconfig)
  * recommended [VS Code](https://code.visualstudio.com) settings and extensions through a [.vscode](./.vscode)
  subdirectory

### [GitHub Actions](./.github/workflows/) CI/CD 🛠️

On any pull request, target a `stg` staging environment and:

* run [ruff](https://github.com/astral-sh/ruff)-based linting and formatting,
[ty](https://github.com/astral-sh/ty)-based type checking, and [pytest](https://docs.pytest.org)-based unit testing;
* perform a [CodeQL](https://codeql.github.com) vulnerability scan;
* build and push a well-labeled container image to a
[Google Cloud Artifact Registry](https://cloud.google.com/artifact-registry/docs);
* execute an integration test on [Google Cloud Run](https://cloud.google.com/run?hl=en) that runs the application
logic end-to-end.

On a commit/tag being merged/pushed (in)to the `main` branch, target a `prd` production environment and:

* perform the same steps as above;
* deploy a Cloud Run job;
* promote the now-vetted container image by adding tags to it such as `latest`, `main` and the
[SemVer](https://semver.org) tag (if any).

## Development 👨‍💻

### Requirements

Install [`uv`](https://docs.astral.sh/uv/getting-started/installation).

### Running the Code

```shell
uv run src/uv_python_project_template/main.py --help  # Display help message.
uv run src/uv_python_project_template/main.py 123     # Compute the 123rd Fibonacci number.
```

### Unit Testing

```shell
uv run --group test pytest                            # Run all `./tests` unit tests and compute a coverage report.
uv run --group test pytest tests/test_utils.py        # Execute (only) the `tests/test_utils.py` unit tests.
uv run --group test pytest --cov-report=xml           # Execute unit tests and write coverage report to `coverage.xml`.
```

### Linting

```shell
uv run --group lint ruff check                        # Lint files.
uv run --group lint ruff check --fix                  # Lint files and fix any fixable errors.
uv run --group lint ruff check --watch                # Lint files and re-lint on change.
uv run --group lint ruff check ${PATH}                # Lint file(s) at `${PATH}`.
```

### Formatting

```shell
uv run --group lint ruff format --check               # Check if files adhere to `ruff` formatting rules.
uv run --group lint ruff format                       # Format files.
uv run --group lint ruff format ${PATH}               # Format file(s) at `${PATH}`.
```

### Type Checking

```shell
uv run --group lint ty check                          # Run type checking.
uv run --group lint ty check --watch                  # Continuously re-run type checking on file change.
uv run --group lint ty check ${PATH}                  # Type check file(s) at `${PATH}`.
```

### Optional [`prek`](https://github.com/j178/prek)-based pre-commit Hooks

Pre-commit hooks that enforce linting, formatting, and type checking before each commit:

```shell
uv run --group pre prek install                       # Set up `prek` hooks.
uv run --group pre prek                               # Run `prek` hooks.
```

### Upgrading Dependencies

```shell
uv lock --upgrade                                     # Upgrade all upgradeable dependencies.
uv lock --upgrade-package ${PACKAGE_NAME}             # Upgrade (only) the `${PACKAGE_NAME}` package.
# Remember to commit the updated uv.lock file.
```

### Bumping the Version

Bump the [SemVer](https://semver.org) version in `project.version` in the [pyproject.toml](pyproject.toml), commit the
change, then create and push a tag:

```shell
git tag -a $(uv version --short) -m 'Descriptive tag message'  # Create a tag.
git push --atomic origin main $(uv version --short)            # Push the tag.
```

Tags must be bare semver strings (e.g. `0.3.1`, not `v0.3.1`). The `$(uv version --short)` command produces the
correct format directly. The CI/CD pipeline validates that the tag matches the `project.version` in `pyproject.toml`
and will fail the deployment if they differ.

## Infrastructure and CI/CD Set-Up 🏗️

See [`docs/INFRASTRUCTURE.md`](docs/INFRASTRUCTURE.md) for GCP project requirements, GitHub Actions secrets/variables,
and IAM role assignments.

## License 🤝

See [LICENSE](LICENSE).
