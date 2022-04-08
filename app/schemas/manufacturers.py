"""Manufacturer schemas."""
import datetime
from typing import Optional

from pydantic import BaseModel


class ManufacturerBase(BaseModel):
    """Manufacturer Base Schema."""

    name: str
    alternate_name: Optional[str]
    country: Optional[str]

    class Config:
        orm_mode = True


class ManufacturerUpdate(BaseModel):
    """Manufacturer Update Schema."""

    pass


class ManufacturerCreate(ManufacturerBase):
    """Manufacturer Create Schema."""

    pass


class Manufacturer(ManufacturerBase):
    """Manufacturer Schema."""

    uuid: str

