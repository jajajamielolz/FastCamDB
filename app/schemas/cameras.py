"""Camera schemas."""
from typing import Optional
from app.schemas.manufacturers import Manufacturer
from app.schemas.manufacturers import ManufacturerCreate
from app.schemas.lenses import LensMountCreate
from app.schemas.lenses import LensMount
from app.schemas.meterings import MeteringCreate
from app.schemas.meterings import Metering
from pydantic import BaseModel


class CameraBase(BaseModel):
    """Camera Base Schema."""

    name: str
    description: Optional[str]
    alternate_name: Optional[str]
    min_shutter_speed: Optional[float]
    max_shutter_speed: Optional[float]
    auto_focus: Optional[bool]
    shutter_priority: Optional[bool]
    aperture_priority: Optional[bool]
    bulb_mode: Optional[bool]
    self_timer: Optional[bool]
    manual: Optional[bool]
    battery_required: Optional[bool]

    class Config:
        orm_mode = True


class CameraUpdate(CameraBase):
    """Camera Update Schema."""
    name: Optional[str]

    pass


class CameraCreate(CameraBase):
    """Camera Create Schema."""
    manufacturer: Optional[ManufacturerCreate]
    lens_mount: Optional[LensMountCreate]
    metering: Optional[MeteringCreate]


class Camera(CameraBase):
    """Camera Schema."""

    uuid: str

    manufacturer: Optional[Manufacturer]
    lens_mount: Optional[LensMount]
    metering: Optional[Metering]

    class Config:
        orm_mode = True


class CameraFilter(BaseModel):
    """Camera Filter Schema."""
    uuid: Optional[str]
    name: Optional[str]
    manufacturer_name: Optional[str]
    lens_mount_name: Optional[str]
    metering_name: Optional[str]

