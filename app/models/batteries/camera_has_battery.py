"""Camera model."""
from sqlalchemy import Column
from sqlalchemy.types import String
from sqlalchemy import ForeignKey

from app.models.core.base import DeclarativeBase
from app.models.core.mixin import UUIDStringPKMixin


class CameraHasBattery(DeclarativeBase, UUIDStringPKMixin):
    """CameraHasBattery model."""

    __tablename__ = "camera_has_battery"

    # foreign keys
    camera_uuid = Column(
        String, ForeignKey("camera.uuid", ondelete="CASCADE"), nullable=False
    )
    battery_uuid = Column(
        String, ForeignKey("battery.uuid", ondelete="CASCADE"), nullable=False
    )
