"""Lens model."""
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import Float
from sqlalchemy.types import String
from sqlalchemy.types import Boolean
from sqlalchemy import DateTime
from sqlalchemy.sql import func


from app.models.core.base import DeclarativeBase
from app.models.core.mixin import UUIDStringPKMixin
from sqlalchemy import ForeignKey


class Lens(DeclarativeBase, UUIDStringPKMixin):
    """Lens model."""

    __tablename__ = "lens"

    # table attributes
    name = Column(String, nullable=True)
    min_aperture = Column(Float, nullable=True)
    max_aperture = Column(Float, nullable=True)
    min_focal_length = Column(Float, nullable=True)
    max_focal_length = Column(Float, nullable=True)
    auto = Column(Boolean, nullable=True)
    manual = Column(Boolean, nullable=True)

    # foreign keys
    lens_mount_uuid = Column(
        String, ForeignKey("lens_mount.uuid", ondelete="CASCADE"), nullable=True
    )
    manufacturer_uuid = Column(
        String, ForeignKey("manufacturer.uuid", ondelete="CASCADE"), nullable=True
    )

    # relationships
    compatible_cameras = relationship(
        "Camera",
        secondary="lens_mount",
        primaryjoin="Lens.lens_mount_uuid == LensMount.uuid",
        secondaryjoin="Camera.lens_mount_uuid == LensMount.uuid",
        viewonly=True,
    )
    lens_mount = relationship("LensMount")
    manufacturer = relationship("Manufacturer")