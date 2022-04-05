"""Mixins."""
from sqlalchemy import Column
from sqlalchemy import String

from app.utils.uuid import generate_uuid_str


class UUIDStringPKMixin(object):
    """DEPRECATED - UUID String Mixin."""

    uuid = Column(String, primary_key=True, default=generate_uuid_str)
