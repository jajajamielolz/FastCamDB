"""Camera model."""
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.types import String
from starlette_context import context

from app.models.core.base import DeclarativeBase
from app.models.core.mixin import UUIDStringPKMixin


class Camera(DeclarativeBase, UUIDStringPKMixin):
    """Camera model."""

    __tablename__ = "camera"

    # table attributes
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    # relationships
    reviews = relationship("Review", back_populates="camera")
