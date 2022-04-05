"""Mixins."""
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Sequence
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID

from app.utils.uuid import generate_uuid_str


class UUIDStringPKMixin(object):
    """DEPRECATED - UUID String Mixin."""

    uuid = Column(String, primary_key=True, default=generate_uuid_str)


