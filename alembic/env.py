import os
import sys

from fastapi import HTTPException

sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # noqa
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

sys.path.append(os.getcwd())  # noqa
from alembic import context  # noqa
from alembic.config import Config  # noqa

# import the model files is all that is needed to take them into account during autogeneration
from app.models.core.base import DeclarativeBase  # noqa


# only really need this for autogeneration so I'm gonna avoid it for now

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
alembic_ini_path = "alembic.ini"
ENVIRONMENT = os.environ.get("ENVIRONMENT")

from app.core.config import config  # noqa

db_host = config.DB_HOSTNAME
db_database = config.DB_DATABASE
db_user = config.DB_SUPERUSER
db_password = config.DB_SUPERPASSWORD
db_type = config.DB_TYPE


dsn = f"{db_type}://{db_user}:{db_password}@{db_host}/{db_database}"


def setup(script_location: str, dsn: str):
    print(
        f"Running DB migrations in {script_location} on {db_host} (environment: {os.environ.get('ENVIRONMENT')})"
    )
    alembic_cfg = Config(alembic_ini_path)
    alembic_cfg.set_main_option("script_location", script_location)
    alembic_cfg.set_main_option("sqlalchemy.url", dsn)
    return alembic_cfg


config = setup("alembic:versions", dsn)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)  # type: ignore

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = DeclarativeBase.metadata


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
