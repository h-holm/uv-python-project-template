# Project Overview

This is a template repository designed to provide a standardized structure for
Python projects.

The application logic (defined under `src/uv_python_project_template`) is
intentionally trivial, as it serves only as a placeholder.

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
