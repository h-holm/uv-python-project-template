# Project Overview

This is a template repository designed to provide a standardized structure for Python projects.

The application logic (defined under `src/uv_python_project_template`) is intentionally trivial, as it serves only as a
placeholder. Although simple, it provides important fundamentals such as a sane logging set-up, a separation of
utilities from core logic, and a clear entry point.

The application logic is covered by rigorous unit tests, as well as an integration test that runs the end-to-end
application logic using a container image built from the source code.

See the `README.md` for full details on development workflows. Refer to the `pyproject.toml` for tooling configuration.

## Structure

* `/src`: Application source code.
* `/tests`: Unit tests.
* `/docs`: Documentation describing the infrastructure set-up.
* `/scripts`: Utility Bash scripts not directly related to the application logic.
* `/.github`: GitHub Actions workflows, Dependabot, CodeQL, GitHub labels, and a pull request (PR) template.
* `/.vscode`: Visual Studio Code settings and recommended extensions.

## Libraries and Frameworks

* `uv` for building and running the application, as well as for managing dependencies and virtual environments.
* `ruff` for linting and code formatting.
* `pytest` for unit testing.
* `ty` for static type checking.
* `prek` for pre-commit hooks to ensure code quality and consistency before commits are made.
* `docker` for building the container image that bundles the application logic and its dependencies.
* Google Cloud Run for deploying and running the application in a serverless environment.
* GitHub Actions for CI/CD.

## Conventions

* Format, lint, and type-check all code with `ruff` and `ty`. Refer to the "Development" section of the `README.md` for
details on how to run these tools.
* Keep commits small and focused on a single issue or feature.
* Keep PRs brief. Minimize diff size.
* Include unit tests for all new or changed code in the same PR as the code changes.
* Unit tests should be simple, straightforward, and brief.
* CI/CD should be set up in such a way that it only runs tests and checks that are relevant to the code changes in the
PR.
* Avoid shortening variable names, e.g., use `version` instead of `ver`, unless the abbreviation is widely recognized
and unambiguous.
