"""Camera model."""
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import Float
from sqlalchemy.types import String
from sqlalchemy.types import Boolean
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey


from app.models.core.base import DeclarativeBase
from app.models.core.mixin import UUIDStringPKMixin


class Camera(DeclarativeBase, UUIDStringPKMixin):
    """Camera model."""

    __tablename__ = "camera"

    # table attributes
    name = Column(String, nullable=True)
    alternate_name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    min_year = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=True
    )
    max_year = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=True
    )
    min_shutter_speed = Column(Float, nullable=True)
    max_shutter_speed = Column(Float, nullable=True)
    auto_focus = Column(Boolean, nullable=True)
    shutter_priority = Column(Boolean, nullable=True)
    aperture_priority = Column(Boolean, nullable=True)
    bulb_mode = Column(Boolean, nullable=True)
    self_timer = Column(Boolean, nullable=True)
    manual = Column(Boolean, nullable=True)
    battery_required = Column(Boolean, nullable=True)

    # foreign keys
    lens_mount_uuid = Column(
        String, ForeignKey("lens_mount.uuid", ondelete="CASCADE"), nullable=True
    )
    manufacturer_uuid = Column(
        String, ForeignKey("manufacturer.uuid", ondelete="CASCADE"), nullable=True
    )
    metering_uuid = Column(
        String, ForeignKey("metering.uuid", ondelete="CASCADE"), nullable=True
    )

    # relationships
    reviews = relationship("Review", back_populates="camera")
    lens_mount = relationship("LensMount")
    manufacturer = relationship("Manufacturer")
    metering = relationship("Metering")
    batteries = relationship(
        "Battery",
        secondary="camera_has_battery",
        primaryjoin="Camera.uuid == CameraHasBattery.camera_uuid",
        secondaryjoin="Battery.uuid == CameraHasBattery.battery_uuid",
        viewonly=True,
    )

    compatible_lenses = relationship(
        "Lens",
        secondary="lens_mount",
        primaryjoin="Camera.lens_mount_uuid == LensMount.uuid",
        secondaryjoin="Lens.lens_mount_uuid == LensMount.uuid",
        viewonly=True,
    )
