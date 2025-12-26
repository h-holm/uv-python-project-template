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

Template repo that enables quick set-up of an end-to-end CI/CD pipeline that (1) tests and (2) deploys a containerized
Python application. The placeholder Python logic computes a Fibonacci number.

## Features ✅

* Environment management and dependency resolution via [uv](https://github.com/astral-sh/uv)
* Primary dependencies and tooling configuration in the [PEP](https://peps.python.org/pep-0621)-recommended
[pyproject.toml](./pyproject.toml) file
* (Sub-)dependency locking in the [uv.lock](./uv.lock) file
* [ruff](https://github.com/astral-sh/ruff)-based linting and formatting
* Static type checking using [mypy](https://github.com/python/mypy)
* [pytest](https://docs.pytest.org) for unit tests with [coverage](https://coverage.readthedocs.io/en/latest)-based
reporting
* Sane and simple logging set-up using [loguru](https://github.com/Delgan/loguru)
* [./src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout) to separate application
logic from tests and other peripherals
* Optional quality-of-life add-ons:
  * automated dependency upgrading and vulnerability scans via [Dependabot](https://github.com/dependabot)
  * [pre-commit](https://github.com/pre-commit/pre-commit) hooks
  * (further) enforcing of uniform formatting via an [.editorconfig](./.editorconfig)
  * recommended [VS Code](https://code.visualstudio.com) settings and extensions through a [.vscode](./.vscode)
  subdirectory

### [GitHub Actions](./.github/workflows/) [CI/CD](https://www.redhat.com/en/topics/devops/what-is-ci-cd) 🛠️

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
uv run --group lint mypy .                            # Run type checking.
uv run --group lint mypy ${PATH}                      # Format file(s) at `${PATH}`.
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
uv lock --upgrade                                     # Upgrade all upgradeable dependencies.
uv lock --upgrade-package ${PACKAGE_NAME}             # Upgrade (only) the `${PACKAGE_NAME}` package.
```

After bumping dependencies, remember to commit the updated [uv.lock](uv.lock) file to version control.

### Bumping the Version

Bump the [SemVer](https://semver.org) version defined in the `project.version` attribute of the
[pyproject.toml](pyproject.toml) configuration. Then, commit the updated config to version control before creating a
`git` tag. Ensure the tag has the same name as the (now bumped) version:

```shell
git tag -a $(uv version --short) -m 'Descriptive tag message'
```

## Infrastructure and CI/CD Set-Up 🏗️

### Necessary Infrastructure

Two [Google Cloud Platform (GCP) projects](https://developers.google.com/workspace/guides/create-project) are
necessary:

* one for staging/testing workloads, and
* another for production workloads.

In each GCP project, the following is required:

* an [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs),
* enablement of the
  [run.googleapis.com](https://docs.cloud.google.com/run/docs/reference/rest#service:-run.googleapis.com) Cloud Run
  API,
* two [service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview):
  * one for running the CI/CD workloads, and
  * another to be used as the identity of the deployed Cloud Run jobs.

### Required GitHub Actions Variables

The [GitHub Actions CI/CD set-up](#github-actions-cicd-🛠️) is split into `stg` and `prd`
[GitHub environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments),
each with a defined set of secrets and variables. In many cases, a secret/variable exists with the same name in both
environments. For instance, a `GCP_PROJECT_ID` is present in both the `stg` and the `prd` environment, just with
different values. In other cases, secrets/variables are set on the repository level. This is the case with, e.g., the
`UV_VERSION` variable, as the `uv` version should be the same in staging as in production workloads.

The following secrets and variables must be available to the GitHub Actions workflows:

* secrets:
  * `GCP_PROJECT_ID`: the ID of the GCP project to target;
  * `GCP_ARTIFACT_REGISTRY_NAME`: the name of the GCP Artifact Registry in which to register container images;
  * `GCP_LOCATION`: the [location/region](https://cloud.google.com/about/locations) of the (1) Artifact Registry to use
  and (2) Cloud Run job(s) to create;
  * `GCP_WORKLOAD_IDENTITY_PROVIDER`: the full identifier of the
  [workload identity federation provider](https://docs.cloud.google.com/iam/docs/workload-identity-federation) through
  which the service accounts authenticate (nota bene: the workload identity provider does _not_ need to exist in the
  same GCP project as the one targeted in the deployment; in fact, the provider can even exist outside of GCP);

* variables:
  * `UV_VERSION`: the [`uv`](https://github.com/astral-sh/uv) version to use in the
  [code quality checks](./.github/workflows/code-quality.yaml);
  * `GCP_CICD_SERVICE_ACCOUNT_NAME`: the name of the GCP service account to assume the identity of in the:
    * [build-and-push-image](./.github/workflows/build-and-push-image.yaml) CI/CD workflow that registers a
      container image in the Artifact Registry,
    * [integration-test](./.github/workflows/integration-test.yaml) and
      [deploy-to-cloud-run](./.github/workflows/deploy-to-cloud-run.yaml) CI/CD workflows that execute Cloud Run jobs;
  * `GCP_RUNTIME_SERVICE_ACCOUNT_NAME`: the name of the GCP service account that the integration test and deployed
  Cloud Run job should assume the identity of (nota bene: to adhere to
  [least privileges best practices](https://en.wikipedia.org/wiki/Principle_of_least_privilege), this identity should
  be different from the `GCP_CICD_SERVICE_ACCOUNT_NAME`).

### Required Roles

The `GCP_CICD_SERVICE_ACCOUNT_NAME` service account requires the following privileges:

* [roles/artifactregistry.admin](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin)
  in order to (1) push images to the Artifact Registry and (2) adjust metadata of existing images;
* [roles/run.developer](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.developer) in order to deploy
  Cloud Run jobs;
* [roles/iam.serviceAccountUser](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) on the
  `GCP_RUNTIME_SERVICE_ACCOUNT_NAME` in order to deploy jobs that assume the identity of the latter.

The workload identity provider requires the following privilege:

* [roles/iam.workloadIdentityUser](https://docs.cloud.google.com/iam/docs/service-account-permissions#workload-identity-user)
  on the `GCP_CICD_SERVICE_ACCOUNT_NAME` in order for the provider to be able to create access tokens on behalf of the
  service account.

## License 🤝

See [LICENSE](LICENSE).
