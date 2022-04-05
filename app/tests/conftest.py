"""Test configuration."""
import os
from typing import Generator

import pytest
from fastapi import Request
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils.functions.database import create_database
from sqlalchemy_utils.functions.database import database_exists
from sqlalchemy_utils.functions.database import drop_database
from starlette_context import context

import alembic.config
from app.api.dependencies.database import get_super_db
from app.api.dependencies.database import get_user_db
from app.core.config import config
from app.core.errors import InvalidTestingEnvironment
from app.main import app
from app.models import DeclarativeBase
from scripts import db_setup

# Show SQL
SHOW_SQL = False

# environment checks
TESTING_ENVIRONMENTS = ["testing", "local"]
ENVIRONMENT = os.environ.get("ENVIRONMENT")


if ENVIRONMENT not in TESTING_ENVIRONMENTS:
    raise InvalidTestingEnvironment(
        environment=ENVIRONMENT, valid_environments=TESTING_ENVIRONMENTS
    )

# ==== Database ====

user_test_conn = (
    f"{config.DB_CONN_METHOD}://{config.DB_USERUSER}:{config.DB_USERPASSWORD}@"
    f"{config.DB_HOSTNAME}/{config.DB_DATABASE}"
)
super_test_conn = (
    f"{config.DB_CONN_METHOD}://{config.DB_SUPERUSER}:{config.DB_SUPERPASSWORD}@"
    f"{config.DB_HOSTNAME}/{config.DB_DATABASE}"
)

super_test_engine = create_engine(super_test_conn, echo=SHOW_SQL)

user_test_engine = create_engine(user_test_conn, echo=SHOW_SQL)

# ==== Database connections ====

# ==== Dependency Overrides ====


def test_requires_auth(request: Request):
    """Override auth dep and add default test user info to request."""
    request.state.user = {
        "user_id": "test_user_main",
        "name": "test user",
        "email": "testuser@fastcamdb.com",
    }
    request.state.user_id = "test_user_main"
    context.state = request.state  # type: ignore


def get_test_db() -> Generator:
    """Return test db session."""
    db = Session(bind=user_test_engine)
    try:
        yield db
    finally:
        db.close()


def test_get_user_confidence_class() -> str:
    """Returns a confidence class."""
    return "verified vasp"


def test_JWTBearer():
    """Passes JWT Check."""
    pass


# ==== Fixtures ====


@pytest.fixture(scope="session", autouse=True)
def verify_env():
    """Verify that environment is a valid testing environment."""
    if ENVIRONMENT not in TESTING_ENVIRONMENTS:
        raise InvalidTestingEnvironment(
            environment=ENVIRONMENT, valid_environments=TESTING_ENVIRONMENTS
        )


@pytest.fixture(scope="session", autouse=True)
def dependency_overrides():
    """Setup Dependency overrides."""
    app.dependency_overrides[get_user_db] = get_test_db
    app.dependency_overrides[get_super_db] = get_test_db


@pytest.fixture(scope="session", autouse=True)
def create_test_db(verify_env):
    """Create a test db."""
    if database_exists(super_test_conn):
        drop_database(super_test_conn)
    create_database(super_test_conn)
    alembic.config.main(argv=["upgrade", "head"])
    db_setup.main()
    for table in DeclarativeBase.metadata.sorted_tables:
        super_test_engine.execute(table.delete())
    print("Test DB setup complete")
    yield
    drop_database(super_test_conn)
    print("Test DB dropped")


@pytest.fixture(scope="session")
def session_db():
    """Return session and tear down after."""
    db = Session(bind=super_test_engine)
    yield db

    for table in DeclarativeBase.metadata.sorted_tables:
        super_test_engine.execute(table.delete())
    db.close()


@pytest.fixture(scope="function")
def test_db():
    """Return session and tear down after."""
    db = Session(bind=super_test_engine)
    yield db

    for table in DeclarativeBase.metadata.sorted_tables:
        super_test_engine.execute(table.delete())
    db.close()


@pytest.fixture(scope="function")
def user_test_db():
    """Return user session and tear down after."""
    db = Session(bind=user_test_engine)
    yield db

    for table in DeclarativeBase.metadata.sorted_tables:
        super_test_engine.execute(table.delete())
    db.close()


@pytest.fixture()
def client():
    """Return test client."""
    yield TestClient(app)
