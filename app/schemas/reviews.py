"""Review schemas."""
import datetime
from typing import Optional

from pydantic import BaseModel


class ReviewBase(BaseModel):
    """Review base schema."""

    description: str


class ReviewCreate(ReviewBase):
    """Review create schema."""

    type_uuid: str

    pass


class ReviewUpdate(BaseModel):
    """Review update schema."""

    description: Optional[str]


class Review(ReviewBase):
    """Review schema."""

    uuid: str
    time_created: datetime.datetime
    time_updated: datetime.datetime

    class Config:
        orm_mode = True
