#!/usr/bin/env bash

SRC_DIR="$(pwd)/src"
APP_DIR="$SRC_DIR/app"

export FASTAPI_CONFIGURATION="TESTING"

# Check if PYTHONPATH is not set or not contain path to src directory
# Src directory can be used to import object for tests, like:
# >>> from tests.something.mock import SomeObjectMock
if [[ -z "$PYTHONPATH" ]] || [[ "$PYTHONPATH" != *"$SRC_DIR"* ]]; then
  export PYTHONPATH="$PYTHONPATH:$SRC_DIR"
fi

# Check if PYTHONPATH is not set or not contain path to app directory
# In tests application object imported using
# >>> from services.something import SomethingService
if [[ -z "$PYTHONPATH" ]] || [[ "$PYTHONPATH" != *"$APP_DIR"* ]]; then
  export PYTHONPATH="$PYTHONPATH:$APP_DIR"
fi

# Run all tests if no arguments overwise send arguments to pytest
if [[ "$#" -eq 0 ]]; then
  poetry run pytest
else
  poetry run pytest "$@"
fi
