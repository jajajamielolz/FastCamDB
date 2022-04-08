"""Battery CRUD."""
from app.models import Battery
from app.schemas import BatteryCreate
from app.schemas import BatteryUpdate
from app.models import CameraHasBattery
from app.schemas import CameraHasBatteryCreate
from app.schemas import CameraHasBatteryUpdate
from app.services.crud.base import CRUDBase


class CRUDBattery(CRUDBase[Battery, BatteryCreate, BatteryUpdate]):
    """Battery crud."""

    pass


class CRUDCameraHasBattery(CRUDBase[CameraHasBattery, CameraHasBatteryCreate, CameraHasBatteryUpdate]):
    """CameraHasBattery crud."""

    pass


battery = CRUDBattery(Battery)

camera_has_battery = CRUDCameraHasBattery(CameraHasBattery)
