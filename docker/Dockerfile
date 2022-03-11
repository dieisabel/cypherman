# Dockerfile for backend application. Intented to use in docker-compose, so it
# doesn't contain CMD, ENTRYPOINT and dont exposing ports

# Base stage where initial preparations are done
FROM python:3.9-slim-bullseye as base

# Stop poetry from creating virtual environment, we dont need it in a container
ENV POETRY_VIRTUALENVS_CREATE false

# Ensure that one see logs in real time
ENV PYTHONBUFFERED 1

# Install curl, so we can download poetry install script. Also remove apt cache
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create a system group and user account for application
RUN groupadd --system app && useradd --system -g app -d /app/ app
WORKDIR /app/
RUN chown -R app:app /app/
USER app

# Add app's local bin to a PATH variable so we can use tools in
# console (poetry, pytest etc)
ENV PATH "${PATH}:/app/.local/bin"

# Copy files with dependencies
COPY pyproject.toml poetry.lock ./

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -


# Stage for development environment where development environment is configured
FROM base as dev

# Prevent python from creating byte code, we don't need it because source code
# will be changing often
ENV PYTHONDONTWRITEBYTECODE 1

# Install development dependencies
RUN poetry install --no-interaction --no-ansi
