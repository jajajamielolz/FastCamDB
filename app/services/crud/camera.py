"""Camera CRUD."""
from app.models import Camera
from app.schemas import CameraCreate
from app.schemas import CameraUpdate
from app.services.crud.base import CRUDBase


class CRUDCamera(CRUDBase[Camera, CameraCreate, CameraUpdate]):
    """Camera crud."""

    pass


camera = CRUDCamera(Camera)
