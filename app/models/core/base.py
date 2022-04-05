"""Declarative Base model."""
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.sql import func
from sqlalchemy_utils import force_instant_defaults

force_instant_defaults()


class Base(object):
    """Base model."""

    time_created = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    time_updated = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )


DeclarativeBase: DeclarativeMeta = declarative_base(cls=Base)
