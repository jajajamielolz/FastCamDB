"""Review model."""
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import String

from app.models.core.base import DeclarativeBase
from app.models.core.mixin import UUIDStringPKMixin


class Review(DeclarativeBase, UUIDStringPKMixin):
    """Review model."""

    __tablename__ = "review"

    # table attributes
    description = Column(String, nullable=False)

    # foreign keys
    camera_uuid = Column(
        String, ForeignKey("camera.uuid", ondelete="CASCADE"), nullable=False
    )

    # relationships
    camera = relationship("Camera", back_populates="reviews")

    @property
    def reviewed_camera_name(self):
        """Name for the camera reviewed."""
        return self.camera.name
