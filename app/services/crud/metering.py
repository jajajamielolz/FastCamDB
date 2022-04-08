"""Metering CRUD."""
from app.models import Metering
from app.schemas import MeteringCreate
from app.schemas import MeteringUpdate
from app.services.crud.base import CRUDBase


class CRUDMetering(CRUDBase[Metering, MeteringCreate, MeteringUpdate]):
    """Metering crud."""

    pass


metering = CRUDMetering(Metering)
