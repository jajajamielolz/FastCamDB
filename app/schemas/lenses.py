"""Lens schemas."""
import datetime
from typing import Optional

from pydantic import BaseModel


class LensBase(BaseModel):
    """Lens Base Schema."""

    name: Optional[str]
    min_focal_length: Optional[float]
    min_focal_length: Optional[float]
    max_focal_length: Optional[float]
    min_aperture: Optional[float]
    max_aperture: Optional[float]
    auto: Optional[bool]
    manual: Optional[bool]
    lens_mount_uuid: Optional[str]
    manufacturer_uuid: Optional[str]

    class Config:
        orm_mode = True


class LensUpdate(BaseModel):
    """Lens Update Schema."""

    pass


class LensCreate(LensBase):
    """Lens Create Schema."""

    pass


class Lens(LensBase):
    """Lens Schema."""

    uuid: str


# ######## camera has battery ########


class LensMountBase(BaseModel):
    """LensMount Base Schema."""

    name: str

    class Config:
        orm_mode = True


class LensMountUpdate(BaseModel):
    """LensMount Update Schema."""

    pass


class LensMountCreate(LensMountBase):
    """LensMount Create Schema."""

    pass


class LensMount(LensMountBase):
    """LensMount Schema."""

    uuid: str

