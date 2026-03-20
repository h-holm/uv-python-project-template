# Project Overview

This project is a Python-based repository template designed to provide a standardized structure and set of conventions
for Python projects. It includes a basic yet straightforward project structure complete with unit tests and a rigorous
integration test that runs the end-to-end application logic on Google Cloud Run using a container image built from the
source code. The CI/CD is set up using GitHub Actions. As described in the `README.md` file at the root of the
repository, the project follows strict code formatting and unit testing guidelines. The goal of the repository is
adherence to best practices, while maintaining simplicity and ease of use for developers. The repository is designed
to be easily adaptable to a wide range of Python projects.

## Folder Structure

* `/src`: The source code / actual application logic.
* `/tests`: Python-based unit tests of the codebase.
* `/.github`: Configuration files for GitHub Actions workflows, Dependabot, CodeQL, and pull requests (PRs), as well as
instructions for coding assistants.
* `/.vscode`: Configuration files for Visual Studio Code, including settings and recommended extensions.

## Libraries and Frameworks

* `uv` for building and running the application, as well as for managing dependencies and virtual environments.
* `pytest` for unit testing.
* `ruff` for linting and code formatting.
* `ty` for static type checking.
* `prek` for pre-commit hooks to ensure code quality and consistency before commits are made.
* `docker` for building and running container images.
* Google Cloud Run for deploying and running the application on Google Cloud Run.
* GitHub Actions for CI/CD.

## Coding Conventions

* Code should be formatted and linted using `ruff`.
* Code should adhere to the `ty` type checking rules.
* Commits should be made in small, focused increments that address a single issue or feature.
* Commit messages should be concise and descriptive.
* PRs should be brief. Aim to minimize the size of the diff.

The `README.md` and `pyproject.toml` files at the root of the repo describe how to ensure adherence to the code
formatting, linting, and type checking conventions.

## Testing

Unit tests should be straightforward, simple and brief. Tests should be added for any new code, and for any changes
to existing code. Tests should be added in the same PR as the code they are testing. Unit tests can be executed locally
using `pytest` as described in the `README.md` file at the root of the repository.
