#!/usr/bin/env bash

poetry add "$@"
poetry export --extras production --format requirements.txt --output requirements.txt
