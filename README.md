# `uv` Python Project Template

[![Python 3.15][python-badge]][python]
[![License: MIT][mit-badge]][mit]
[![uv][uv-badge]][uv]
[![Ruff][ruff-badge]][ruff]
[![ty][ty-badge]][ty]
[![Pytest][pytest-badge]][pytest]
[![prek][prek-badge]][prek]
[![CI/CD][ci-cd-badge]][ci-cd]
[![CodeQL][codeql-badge]][codeql-workflow]
[![pre-commit.ci status][pre-commit-ci-badge]][pre-commit-ci]

Template repo that enables quick set-up of an end-to-end CI/CD pipeline that
(1) tests and (2) deploys a containerized Python application. The placeholder
Python logic computes a Fibonacci number.

## Features ✅

- Environment management and dependency resolution via [uv][uv]
- [pyproject.toml](./pyproject.toml) for dependencies and tooling configuration
- Dependency locking via [uv.lock](./uv.lock)
- [ruff][ruff]-based linting and formatting
- Type checking using [ty][ty]
- [pytest][pytest]-powered unit tests with [coverage][coverage]-based reporting
- Structured logging via [Loguru][loguru]
- [./src layout][src-layout] to separate application logic from peripherals
- Optional quality-of-life add-ons:
  - automated dependency updates and vulnerability scans via [Dependabot][dep]
  - comprehensive [prek][prek]-based pre-commit hooks
  - (further) enforcing of uniform formatting via an
    [.editorconfig](./.editorconfig)
  - recommended [VS Code][vscode] settings under [.vscode](./.vscode)
  - default [LLM][llm] coding agent instructions in [AGENTS.md](./AGENTS.md)
    with model-specific extended instructions in [CLAUDE.md](.claude/CLAUDE.md)
    and [.github/copilot-instructions.md](.github/copilot-instructions.md)

### [GitHub Actions][github-actions] CI/CD 🛠️

On any pull request, target a `stg` staging environment and:

- run `ruff`-based linting and formatting, `ty`-based type checking, and
  `pytest`-based unit testing;
- perform a [CodeQL][codeql] vulnerability scan;
- build and push a well-labeled container image to a
  [Google Cloud Artifact Registry][gcp-artifact-registry];
- execute an end-to-end integration test by triggering a one-off
  [Google Cloud Run][gcp-cloud-run] job that runs the application logic
  end-to-end using the newly built container image.

On a commit being merged/pushed into the `main` branch, target a `prd`
production environment and:

- perform the same steps as above;
- tag the now-vetted container image with `main`;
- if the commit introduces a new version in the `pyproject.toml`, release it:
  - tag the commit with the version `<major>.<minor>.<patch>`;
  - deploy the vetted container image as a Cloud Run job;
  - tag the deployed container image with the [SemVer][semver] tags
    `<major>.<minor>.<patch>`, `<major>.<minor>` and `<major>`, and `latest`;
  - create a GitHub Release named `Release <major>.<minor>.<patch>` with
    auto-generated release notes listing the PRs merged since the previous
    release.

## Development 👨‍💻

### Requirements

Install [`uv`][uv-install].

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

### Optional [`prek`][prek]-based pre-commit Hooks

Pre-commit hooks that enforce linting, formatting, and type checking before
each commit:

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

### Releasing a New Version

The version in the `pyproject.toml` controls releases. To release a new
version, bump it in a PR:

```shell
uv version --bump patch  # Bump the patch version (e.g. 0.4.1 -> 0.4.2).
uv version --bump minor  # Bump the minor version (e.g. 0.4.1 -> 0.5.0).
uv version --bump major  # Bump the major version (e.g. 0.4.1 -> 1.0.0).
```

Commit the updated `pyproject.toml` and `uv.lock` files and open a PR. The PR
checks fail if the version is not of the form `<major>.<minor>.<patch>` or is
lower than the latest released version. Once the PR is merged and the vetted
image has passed the integration test on `main`, the CI/CD pipeline releases the
new version as described in the CI/CD section above. Do not create version tags
manually; the pipeline creates them.

If a deployment fails, re-run the failed jobs of the workflow run. To roll back
to (or redeploy) an already-released version, run the
[Deploy to Cloud Run][deploy] workflow manually with that version as input.

## Infrastructure and CI/CD Set-Up 🏗️

See [`docs/INFRASTRUCTURE.md`](docs/INFRASTRUCTURE.md) for GCP project
requirements, GitHub Actions secrets/variables, and IAM role assignments.

## License 🤝

See [LICENSE](LICENSE).

[//]: # (References)

[ci-cd]: https://github.com/h-holm/uv-python-project-template/actions/workflows/ci-cd.yaml
[ci-cd-badge]: https://github.com/h-holm/uv-python-project-template/actions/workflows/ci-cd.yaml/badge.svg
[codeql]: https://codeql.github.com
[codeql-badge]: https://github.com/h-holm/uv-python-project-template/workflows/CodeQL%20Analysis/badge.svg
[codeql-workflow]: https://github.com/h-holm/uv-python-project-template/actions/workflows/codeql-analysis.yaml
[coverage]: https://coverage.readthedocs.io/en/latest
[dep]: https://github.com/dependabot
[deploy]: https://github.com/h-holm/uv-python-project-template/actions/workflows/deploy-to-cloud-run.yaml
[gcp-artifact-registry]: https://cloud.google.com/artifact-registry/docs
[gcp-cloud-run]: https://cloud.google.com/run?hl=en
[github-actions]: https://docs.github.com/en/actions
[llm]: https://en.wikipedia.org/wiki/Language_model
[loguru]: https://github.com/Delgan/loguru
[mit]: https://opensource.org/licenses/MIT
[mit-badge]: https://img.shields.io/badge/License-MIT-9400d3.svg
[pre-commit-ci]: https://results.pre-commit.ci/latest/github/h-holm/uv-python-project-template/main
[pre-commit-ci-badge]: https://results.pre-commit.ci/badge/github/h-holm/uv-python-project-template/main.svg
[prek]: https://github.com/j178/prek
[prek-badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json
[pytest]: https://docs.pytest.org
[pytest-badge]: https://img.shields.io/static/v1?label=%E2%80%8E&message=Pytest&logo=Pytest&color=b647c4&logoColor=white
[python]: https://docs.python.org/3/whatsnew/3.15.html
[python-badge]: https://img.shields.io/badge/python-3.15-blue.svg
[ruff]: https://github.com/astral-sh/ruff
[ruff-badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[semver]: https://semver.org
[src-layout]: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout
[ty]: https://github.com/astral-sh/ty
[ty-badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json
[uv]: https://github.com/astral-sh/uv
[uv-badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json
[uv-install]: https://docs.astral.sh/uv/getting-started/installation
[vscode]: https://code.visualstudio.com
