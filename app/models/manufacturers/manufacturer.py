"""Manufacturer model."""
from sqlalchemy import Column
from sqlalchemy.types import String
from sqlalchemy.types import Integer


from app.models.core.base import DeclarativeBase
from app.models.core.mixin import UUIDStringPKMixin


class Manufacturer(DeclarativeBase, UUIDStringPKMixin):
    """Manufacturer model."""

    __tablename__ = "manufacturer"

    # table attributes
    name = Column(String, nullable=True)
    alternate_name = Column(String, nullable=True)
    country = Column(String, nullable=True)
