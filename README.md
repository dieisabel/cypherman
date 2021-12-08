# Cypherman

### Dependencies

For working with dependencies we use [poetry](https://python-poetry.org/).

All dependencies listed in [pyproject.toml](https://github.com/dieisabel/cypherman/blob/develop/pyproject.toml)
in `tool.poetry.dependencies` section.

### Installation

Clone a project using `git clone https://github.com/dieisabel/cypherman`.

Use poetry to create a virtual environment and install there production dependencies with `poetry install`.

### Development

Clone a project using `git clone https://github.com/dieisabel/cypherman`.

Use poetry to create a virtual environment and install there development dependencies with `poetry install --dev`.

To start FastAPI development server firstly change current directory to application directory with `cd src/app/`,
then start server using `poetry run uvicorn main:application --reload`.

Also project contains [editorconfig file](https://editorconfig.org/), so make sure your editor supports it.

### License

This project is licensed under the terms of the MIT license.
