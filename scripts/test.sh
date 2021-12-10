#!/usr/bin/env bash

APP_DIR="$(pwd)/src/app"

# Check if PYTHONPATH is not set or not contain path to app directory
if [[ -z "$PYTHONPATH" ]] || [[ "$PYTHONPATH" != *"$APP_DIR"* ]]; then
  export PYTHONPATH="$PYTHONPATH:$APP_DIR"
fi

# Run all tests if no arguments overwise send arguments to pytest
if [[ "$#" -eq 0 ]]; then
  poetry run pytest
else
  poetry run pytest "$*"
fi
