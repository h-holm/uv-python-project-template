# Infrastructure and CI/CD Set-Up 🏗️

This document describes the [Google Cloud Platform (GCP)][gcp] infrastructure
set-up and [GitHub Actions][github-actions] configuration required by the CI/CD
pipelines defined in [`.github/workflows/`](../.github/workflows). For general
development instructions, see the [README](../README.md).

## Necessary Infrastructure

Two [GCP projects][gcp-projects] are necessary:

- one for staging/testing workloads, and
- another for production workloads.

In each GCP project, the following is required:

- an [Artifact Registry][gcp-artifact-registry],
- enablement of the [run.googleapis.com][gcp-run-api] Cloud Run API,
- two [service accounts][gcp-service-accounts]:
  - one for running the CI/CD workloads, and
  - another to be used as the identity of the deployed Cloud Run jobs.

## Required GitHub Actions Variables

The CI/CD set-up uses `stg` and `prd` [GitHub environments][github-envs], each
with their own set of secrets and variables.

The following secrets and variables must be available to the GitHub Actions
workflows:

- secrets:
  - `GCP_PROJECT_ID`: the ID of the GCP project to target;
  - `GCP_ARTIFACT_REGISTRY_NAME`: the name of the GCP Artifact Registry in
    which to register container images;
  - `GCP_LOCATION`: the [location/region][gcp-locations] of the (1) Artifact
    Registry to use and (2) Cloud Run job(s) to create;
  - `GCP_WORKLOAD_IDENTITY_PROVIDER`: the full identifier of the
    [Workload Identity Federation][gcp-wif] provider through which the service
    accounts authenticate (the provider does not need to exist in the same GCP
    project as the deployment target);

- variables:
  - `GCP_CICD_SERVICE_ACCOUNT_NAME`: the name of the GCP service account to
    assume the identity of in the:
    - [build-and-push-image](../.github/workflows/build-and-push-image.yaml)
      workflow that registers a container image in the Artifact Registry,
    - [integration-test](../.github/workflows/integration-test.yaml) and
      [deploy-to-cloud-run](../.github/workflows/deploy-to-cloud-run.yaml)
      workflows that execute Cloud Run jobs;
  - `GCP_RUNTIME_SERVICE_ACCOUNT_NAME`: the name of the GCP service account
    that the integration test and deployed Cloud Run job assume the identity
    of. To follow [least-privilege principles][least-privilege], this should be
    a separate account from `GCP_CICD_SERVICE_ACCOUNT_NAME`.

## Required Roles

The `GCP_CICD_SERVICE_ACCOUNT_NAME` service account requires:

- [roles/artifactregistry.admin][gcp-registry-admin] to push images to and
  update metadata in the Artifact Registry;
- [roles/run.developer][gcp-run-developer] to deploy Cloud Run jobs;
- [roles/iam.serviceAccountUser][gcp-service-account-user] on the
  `GCP_RUNTIME_SERVICE_ACCOUNT_NAME` to deploy jobs that run as that identity.

The workload identity provider requires:

- [roles/iam.workloadIdentityUser][gcp-workload-identity-user] on the
  `GCP_CICD_SERVICE_ACCOUNT_NAME` to generate access tokens on its behalf.

[//]: # (References)

[gcp]: https://cloud.google.com
[gcp-artifact-registry]: https://docs.cloud.google.com/artifact-registry/docs
[gcp-locations]: https://cloud.google.com/about/locations
[gcp-projects]: https://developers.google.com/workspace/guides/create-project
[gcp-registry-admin]: https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin
[gcp-run-api]: https://docs.cloud.google.com/run/docs/reference/rest#service:-run.googleapis.com
[gcp-run-developer]: https://docs.cloud.google.com/run/docs/reference/iam/roles#run.developer
[gcp-service-account-user]: https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role
[gcp-service-accounts]: https://docs.cloud.google.com/iam/docs/service-account-overview
[gcp-wif]: https://docs.cloud.google.com/iam/docs/workload-identity-federation
[gcp-workload-identity-user]: https://docs.cloud.google.com/iam/docs/service-account-permissions#workload-identity-user
[github-actions]: https://docs.github.com/en/actions
[github-envs]: https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments
[least-privilege]: https://en.wikipedia.org/wiki/Principle_of_least_privilege
