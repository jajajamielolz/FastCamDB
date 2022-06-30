"""Lens schemas."""
from typing import Optional
from pydantic import BaseModel
from app.schemas.manufacturers import ManufacturerCreate
from app.schemas.manufacturers import Manufacturer
from typing import List

class LensMountBase(BaseModel):
    """LensMount Base Schema."""

    name: str = "M42 | K-mount | C/Y | Yashica AF | MC/MD | Konica AR"

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

    class Config:
        orm_mode = True


class LensBase(BaseModel):
    """Lens Base Schema."""

    name: Optional[str]
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


class LensUpdate(LensBase):
    """Lens Update Schema."""

    pass


class LensCreate(BaseModel):
    """Lens Create Schema."""
    manufacturer: Optional[ManufacturerCreate]
    lens_mount: Optional[LensMountCreate]
    name: Optional[str]
    min_focal_length: Optional[float]
    max_focal_length: Optional[float]
    min_aperture: Optional[float]
    max_aperture: Optional[float]
    auto: Optional[bool]
    manual: Optional[bool]

    class Config:
        orm_mode = True


class CameraPreview(BaseModel):
    """Camera Preview Model"""
    uuid: str
    name: str

    class Config:
        orm_mode = True


class Lens(LensBase):
    """Lens Schema."""
    uuid: str
    manufacturer: Optional[Manufacturer]
    lens_mount: Optional[LensMount]
    compatible_cameras: Optional[List[CameraPreview]]

    class Config:
        orm_mode = True


class LensFilter(LensBase):
    """Lens Filter Schema."""
    uuid: Optional[str]
    manufacturer_name: Optional[str]
    lens_mount_name: Optional[str]
