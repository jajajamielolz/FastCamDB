"""Manufacturer CRUD."""
from app.models import Manufacturer
from app.schemas import ManufacturerCreate
from app.schemas import ManufacturerUpdate
from app.services.crud.base import CRUDBase


class CRUDManufacturer(CRUDBase[Manufacturer, ManufacturerCreate, ManufacturerUpdate]):
    """Manufacturer crud."""

    pass


manufacturer = CRUDManufacturer(Manufacturer)
