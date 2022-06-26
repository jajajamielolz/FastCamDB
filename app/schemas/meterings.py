"""Metering schemas."""
import datetime
from typing import Optional

from pydantic import BaseModel


class MeteringBase(BaseModel):
    """Metering Base Schema."""

    name: str = "Spot | Center-Weighted | Matrix | Evaluative | CLC (Contrast Light Compensation)"
    description: Optional[str]

    class Config:
        orm_mode = True


class MeteringUpdate(BaseModel):
    """Metering Update Schema."""

    pass


class MeteringCreate(MeteringBase):
    """Metering Create Schema."""

    pass


class Metering(MeteringBase):
    """Metering Schema."""

    uuid: str

