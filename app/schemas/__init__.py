"""Pydantic validation schemas used by API and CRUD services."""
from .cameras import Camera  # noqa
from .cameras import CameraBase  # noqa
from .cameras import CameraCreate  # noqa
from .cameras import CameraUpdate  # noqa
from .cameras import CameraFilter  # noqa
from .reviews import Review  # noqa
from .reviews import ReviewBase  # noqa
from .reviews import ReviewCreate  # noqa
from .reviews import ReviewUpdate  # noqa

from .batteries import Battery  # noqa
from .batteries import BatteryBase  # noqa
from .batteries import BatteryCreate  # noqa
from .batteries import BatteryUpdate  # noqa
from .batteries import CameraHasBattery  # noqa
from .batteries import CameraHasBatteryBase  # noqa
from .batteries import CameraHasBatteryCreate  # noqa
from .batteries import CameraHasBatteryUpdate  # noqa


from .lenses import Lens  # noqa
from .lenses import LensBase  # noqa
from .lenses import LensCreate  # noqa
from .lenses import LensUpdate  # noqa
from .lenses import LensFilter  # noqa
from .lenses import LensMount  # noqa
from .lenses import LensMountBase  # noqa
from .lenses import LensMountCreate  # noqa
from .lenses import LensMountUpdate  # noqa

from .manufacturers import Manufacturer  # noqa
from .manufacturers import ManufacturerBase  # noqa
from .manufacturers import ManufacturerCreate  # noqa
from .manufacturers import ManufacturerUpdate  # noqa

from .meterings import Metering  # noqa
from .meterings import MeteringBase  # noqa
from .meterings import MeteringCreate  # noqa
from .meterings import MeteringUpdate  # noqa