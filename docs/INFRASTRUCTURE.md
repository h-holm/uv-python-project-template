# Infrastructure and CI/CD Set-Up 🏗️

This document describes the Google Cloud Platform (GCP) infrastructure and GitHub Actions configuration required by the
CI/CD pipelines defined in [`.github/workflows/`](../.github/workflows/). For general development instructions, see the
[README](../README.md).

## Necessary Infrastructure

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

## Required GitHub Actions Variables

The CI/CD set-up uses `stg` and `prd`
[GitHub environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments),
each with their own secrets and variables.

The following secrets and variables must be available to the GitHub Actions workflows:

* secrets:
  * `GCP_PROJECT_ID`: the ID of the GCP project to target;
  * `GCP_ARTIFACT_REGISTRY_NAME`: the name of the GCP Artifact Registry in which to register container images;
  * `GCP_LOCATION`: the [location/region](https://cloud.google.com/about/locations) of the (1) Artifact Registry to use
  and (2) Cloud Run job(s) to create;
  * `GCP_WORKLOAD_IDENTITY_PROVIDER`: the full identifier of the
  [workload identity federation provider](https://docs.cloud.google.com/iam/docs/workload-identity-federation) through
  which the service accounts authenticate (the provider does not need to exist in the same GCP project as the
  deployment target);

* variables:
  * `GCP_CICD_SERVICE_ACCOUNT_NAME`: the name of the GCP service account to assume the identity of in the:
    * [build-and-push-image](../.github/workflows/build-and-push-image.yaml) CI/CD workflow that registers a
      container image in the Artifact Registry,
    * [integration-test](../.github/workflows/integration-test.yaml) and
      [deploy-to-cloud-run](../.github/workflows/deploy-to-cloud-run.yaml) CI/CD workflows that execute Cloud Run jobs;
  * `GCP_RUNTIME_SERVICE_ACCOUNT_NAME`: the name of the GCP service account that the integration test and deployed
  Cloud Run job should assume the identity of. To follow
  [least-privilege principles](https://en.wikipedia.org/wiki/Principle_of_least_privilege), this should be a separate
  account from `GCP_CICD_SERVICE_ACCOUNT_NAME`.

## Required Roles

The `GCP_CICD_SERVICE_ACCOUNT_NAME` service account requires:

* [roles/artifactregistry.admin](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin)
  to push images to and update metadata in the Artifact Registry;
* [roles/run.developer](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.developer) to deploy Cloud Run
  jobs;
* [roles/iam.serviceAccountUser](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) on the
  `GCP_RUNTIME_SERVICE_ACCOUNT_NAME` to deploy jobs that run as that identity.

The workload identity provider requires:

* [roles/iam.workloadIdentityUser](https://docs.cloud.google.com/iam/docs/service-account-permissions#workload-identity-user)
  on the `GCP_CICD_SERVICE_ACCOUNT_NAME` to generate access tokens on its behalf.
