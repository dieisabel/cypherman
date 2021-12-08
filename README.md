# Cypherman

### Description

Cypherman is a RESTful API for hashing, encrypting and more! API that allows to work with cybersecurity!

The goal of project is practice creating and deploying REST api using Python and it's ecosystem.

**First release must be done before 21.11.21**

### Plans

#### Features

- Hashes: user can hash data using various of hashing algorithms.
- Encryption: user can encrypt data using various of encryption algorithms.
- Random password generation: user can generate random password.

### Technologies

- Python 3.9
- FastAPI
- SQLAlchemy

For working with dependencies we use [poetry](https://python-poetry.org/).

All production dependencies listed in [pyproject.toml](https://github.com/dieisabel/cypherman/blob/develop/pyproject.toml)
in `tool.poetry.dependencies` section. All development dependencies listed in `tool.dependencies.dev-dependencies` section.

### Installation

Clone a project using `git clone https://github.com/dieisabel/cypherman`.

Use poetry to create a virtual environment and install there production dependencies with `poetry install`.

### Development

Clone a project using `git clone https://github.com/dieisabel/cypherman`.

Use poetry to create a virtual environment and install there development dependencies with `poetry install --dev`.

Also project contains [editorconfig file](https://editorconfig.org/), so make sure your editor supports it.

### Documentation

Documentation located in `docs/` directory.

### License

This project is licensed under the terms of the MIT license.
