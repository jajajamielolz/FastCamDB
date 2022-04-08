"""LensMount model."""
from sqlalchemy import Column
from sqlalchemy.types import String
from sqlalchemy.types import Integer


from app.models.core.base import DeclarativeBase
from app.models.core.mixin import UUIDStringPKMixin


class LensMount(DeclarativeBase, UUIDStringPKMixin):
    """LensMount model."""

    __tablename__ = "lens_mount"

    # table attributes
    name = Column(String, nullable=True)
