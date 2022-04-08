"""Battery model."""
from sqlalchemy import Column
from sqlalchemy.types import Float
from sqlalchemy.types import String


from app.models.core.base import DeclarativeBase
from app.models.core.mixin import UUIDStringPKMixin


class Battery(DeclarativeBase, UUIDStringPKMixin):
    """Battery model."""

    __tablename__ = "battery"

    # table attributes
    name = Column(String, nullable=True)
    voltage = Column(Float, nullable=True)