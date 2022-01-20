import pytest

from sqlalchemy.orm import Session

from core.db import DatabaseSession


@pytest.fixture
def session() -> Session:
    return DatabaseSession()
