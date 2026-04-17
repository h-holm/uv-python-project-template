# Project Overview

This is a template repository designed to provide a standardized structure for
Python projects.

The application logic (defined under `src/uv_python_project_template`) is
intentionally trivial, as it serves only as a placeholder. Although simple, it
provides important fundamentals such as a sane logging set-up, a separation of
utilities from core logic, and a clear entry point.

The application logic is covered by rigorous unit tests, as well as an
integration test that runs the end-to-end application logic using a container
image built from the source code.

## Structure

* `/src`: Application source code.
* `/tests`: Unit tests.
* `/docs`: Documentation describing the infrastructure set-up.
* `/scripts`: Utility Bash scripts not directly related to the core logic.
* `/.github`: GitHub Actions configurations and CI/CD workflow definitions.

## Libraries, Frameworks and Conventions

See the `README.md` for details on the development workflow. Refer to the
`pyproject.toml` for exact tooling configuration.

* Keep commits small and focused on a single issue or feature.
* Keep PRs brief. Minimize diff size.
* Include unit tests for all new or changed code in the same PR as the code
  changes.
* Unit tests should be simple and straightforward.
* CI/CD should be configured to only run tests and checks that are relevant to
  the code changes in the PR.
* Avoid shortening variable names, e.g., use `version` instead of `ver`, unless
  the abbreviation is widely recognized and unambiguous.
