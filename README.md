# Cypherman

## Table of contents

1. [Description](#description)
2. [Production](#production)
   1. [Production tools](#production-tools)
   2. [Heroku](#heroku)
   3. [Installation for production](#installation-for-production)
   4. [Deploying](#deploying)
   5. [Production local testing](#production-local-testing)
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

All production dependencies listed in `pyproject.toml` in `tool.poetry.extras` section in `production` list.
All development dependencies listed in `tool.dependencies.dev-dependencies` section.
For installing dependencies use `scripts/poetry-add.sh` script.

### Production

#### Production tools

All tools that are used in production are listed in `pyproject.toml` in `tool.poetry.extras` in a `production` list.
Here is a list with dependencies, and it's usage:

- [Gunicorn](https://gunicorn.org/). Running Uvicorn using a process manager ensures that you can run multiple processes
  in a resilient manner, and allows you to perform server upgrades without dropping requests.

Config files for production tools located in `deploy/` directory.

#### Heroku

For production, we use Heroku platform. So, make sure you are familiar with it at least at basic level.
See [Getting started on Heroku with python](https://devcenter.heroku.com/articles/getting-started-with-python).

Here I try to describe basic files that Heroku needs to successfully build, release and run application:

- [Procfile](https://devcenter.heroku.com/articles/procfile). Heroku app include a Procfile that specifies the commands that are executed by the app on startup.
- [runtime.txt](https://devcenter.heroku.com/articles/python-runtimes). Contains python version.
- requirements.txt. Contains dependencies.

Also, don't forget to create Heroku account and create there new application.

#### Installation for production

Clone a project using `git clone https://github.com/dieisabel/cypherman`.

Use poetry to create a virtual environment and install there production dependencies with
`poetry install --no-dev --extra production`.

#### Deploying

For deploying use Git and Heroku. But before this install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
and login to your Heroku account.

The main idea of deploying project with git is that you add Heroku git remote and push there your branch.

The process of deploying application with Heroku platform fully described [here](https://devcenter.heroku.com/articles/git),
but I'll briefly rewrite these steps here:

1. Add Heroku remote `heroku git:remote -a <application name>`
2. Push branch to Heroku remote `git push heroku main`. If you need to push branch which is not master, use
   `git push heroku <your branch>:main`.

Also remember that Heroku have some limits, you can see them [here](https://devcenter.heroku.com/articles/git#repository-size).

#### Production local testing

If you want to test application in production environment use [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
Follow these steps:

1. Activate virtual environment using `poetry shell` or manually `./.venv/bin/activate`.
2. Run `heroku local`. It will read all needed files and load environment variables from `.env`.

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
