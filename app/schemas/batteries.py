"""Battery schemas."""
import datetime
from typing import Optional

from pydantic import BaseModel


class BatteryBase(BaseModel):
    """Battery Base Schema."""

    name: Optional[str]
    voltage: Optional[float]

    class Config:
        orm_mode = True


class BatteryUpdate(BaseModel):
    """Battery Update Schema."""

    pass


class BatteryCreate(BatteryBase):
    """Battery Create Schema."""

    pass


class Battery(BatteryBase):
    """Battery Schema."""

    uuid: str


# ######## camera has battery ########


class CameraHasBatteryBase(BaseModel):
    """CameraHasBattery Base Schema."""

    battery_uuid: str
    camera_uuid: str

    class Config:
        orm_mode = True


class CameraHasBatteryUpdate(BaseModel):
    """CameraHasBattery Update Schema."""

    pass


class CameraHasBatteryCreate(CameraHasBatteryBase):
    """CameraHasBattery Create Schema."""

    pass


class CameraHasBattery(CameraHasBatteryBase):
    """CameraHasBattery Schema."""

    uuid: str

