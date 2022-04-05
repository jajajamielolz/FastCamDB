"""Camera schemas."""
import datetime
from typing import Optional

from pydantic import BaseModel


class CameraBase(BaseModel):
    """Camera Base Schema."""

    name: str
    description: Optional[str]

    class Config:
        orm_mode = True


class CameraUpdate(BaseModel):
    """Camera Update Schema."""

    pass


class CameraCreate(CameraBase):
    """Camera Create Schema."""

    pass


class Camera(CameraBase):
    """Camera Schema."""

    uuid: str
    time_created: datetime.datetime
    time_updated: datetime.datetime
