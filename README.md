# Cypherman

## Table of contents

1. [Description](#description)
2. [Production](#production)
3. [Development](#development)
4. [Testing](#testing)
5. [Documentation](#documentation)
6. [License](#license)

### Description

Cypherman is a RESTful API for hashing, encrypting and more! API that allows to work with cybersecurity!

The goal of project is practice creating and deploying REST api using Python and it's ecosystem.

#### Features

- Hashes: user can hash data using various of hashing algorithms.

### Technologies

- Python
- FastAPI

For working with dependencies we use [poetry](https://python-poetry.org/).

All production dependencies listed in [pyproject.toml](https://github.com/dieisabel/cypherman/blob/develop/pyproject.toml)
in `tool.poetry.dependencies` section. All development dependencies listed in `tool.dependencies.dev-dependencies` section.

### Production

Clone a project using `git clone https://github.com/dieisabel/cypherman`.

Use poetry to create a virtual environment and install there production dependencies with `poetry install --no-dev`.

### Development

Clone a project using `git clone https://github.com/dieisabel/cypherman`.

Use poetry to create a virtual environment and install there development dependencies with `poetry install --dev`.

To run development server go to app folder using `cd /src/app/` and run `poetry run uvicorn main:application --reload`.

#### Code style

Project contains [editorconfig file](https://editorconfig.org/), so make sure your editor supports it. In project we set:
- Line length is 120
- CamelCase for classes
- snake_case for functions and methods

### Testing

For testing code we use `pytest`. All tests must be located in `src/tests` directory. To run tests use
testing script, which is located in `scripts/test.sh`.

#### Naming conventions

For test classes use Test* naming. For methods (which are tests) use test_* naming.

### Documentation

Documentation located in `docs/` directory. Also, by FastAPI we can autogenerate OpenAPI docs.
To access them run development server (see [Development](#development)) and go to `/docs` for SwaggerUI or
to `/redoc` for ReDoc. Also, FastAPI allows us to add metadata and docs urls, for more information see
[Metadata and Docs URLS](https://fastapi.tiangolo.com/tutorial/metadata/).

### License

This project is licensed under the terms of the MIT license.
