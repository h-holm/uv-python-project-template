# syntax=docker.io/docker/dockerfile:1
# Inspired by: https://github.com/astral-sh/uv-docker-example/blob/main/Dockerfile

# Use an image with `uv` pre-installed.
FROM ghcr.io/astral-sh/uv:0.9-python3.14-alpine

# Setup a non-root user.
RUN addgroup -S -g 1000 nonroot \
    && adduser -S -D -G nonroot -u 1000 -h /home/nonroot nonroot

# Install the project into `/app`.
WORKDIR /app

# Enable bytecode compilation to improve startup time (at the cost of increased installation time).
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since a mounted volume is used.
ENV UV_LINK_MODE=copy

# Omit development dependencies.
ENV UV_NO_DEV=1

# Ensure installed tools can be executed out of the box.
ENV UV_TOOL_BIN_DIR=/usr/local/bin

# Install the project dependencies using the `uv.lock` lockfile and `pyproject.toml` settings.
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

# Add (only) the project source code and install it. Installing separately from the dependencies allows optimal layer
# caching.
COPY ./src /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

# Place environment executables at the front of the `$PATH`.
ENV PATH="/app/.venv/bin:$PATH"

# Use the non-root user to run our application
USER nonroot

ENTRYPOINT [ "uv", "run", "src/uv_python_project_template/main.py" ]

LABEL name="uv-python-project-template"
LABEL maintainer="https://github.com/h-holm"
LABEL description="A template Python project using `uv`"
LABEL url="https://github.com/h-holm/uv-python-project-template"
