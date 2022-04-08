"""Battery CRUD."""
from app.models import Lens
from app.schemas import LensCreate
from app.schemas import LensUpdate
from app.models import LensMount
from app.schemas import LensMountCreate
from app.schemas import LensMountUpdate
from app.services.crud.base import CRUDBase


class CRUDLens(CRUDBase[Lens, LensCreate, LensUpdate]):
    """Lens crud."""

    pass


class CRUDLensMount(CRUDBase[LensMount, LensMountCreate, LensMountUpdate]):
    """LensMount crud."""

    pass


lens = CRUDLens(Lens)

lens_mount = CRUDLensMount(LensMount)
