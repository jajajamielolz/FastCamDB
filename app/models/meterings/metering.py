"""Metering model."""
from sqlalchemy import Column
from sqlalchemy.types import String


from app.models.core.base import DeclarativeBase
from app.models.core.mixin import UUIDStringPKMixin


class Metering(DeclarativeBase, UUIDStringPKMixin):
    """Metering model."""

    __tablename__ = "metering"

    # table attributes
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)