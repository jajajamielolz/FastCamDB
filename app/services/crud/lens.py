"""Lens CRUD."""
from app.models import Lens
from app.schemas import LensCreate
from app.schemas import LensUpdate
from app.models import LensMount
from app.schemas import LensMountCreate
from app.schemas import LensMountUpdate
from app.services.crud.base import CRUDBase
from sqlalchemy.orm import Session
from app.core import errors
from app.services import crud
from app import schemas
from sqlalchemy import desc


class CRUDLens(CRUDBase[Lens, LensCreate, LensUpdate]):
    """Lens crud."""
    def create_lens(self, obj_in: LensCreate, db: Session) -> Lens:
        """Create a lens."""
        # check if lens with the same name exists first
        exists = self.get(db=db, get_property="name", get_value=obj_in.name)
        if exists:
            raise errors.DuplicateObjectError(name=exists.name, uuid=exists.uuid, object_type="Lens")
        lens_obj = self.create(obj_in=obj_in, db=db)
        if obj_in.manufacturer:
            manufacturer = crud.manufacturer.get_or_create(db=db, obj_in=obj_in.manufacturer, get_property="name")
            lens_obj.manufacturer_uuid = manufacturer.uuid
        if obj_in.lens_mount:
            lens_mount = crud.lens_mount.get_or_create(db=db, obj_in=obj_in.lens_mount, get_property="name")
            lens_obj.lens_mount_uuid = lens_mount.uuid
        db.commit()
        return lens_obj
    
    def filter_lens(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 100,
        custom_filter: schemas.LensFilter = None,
    ) -> Lens:
        """
        Get a list of model objects.

        :param custom_filter: parameters to filter lenss
        :param db: a db session
        :param skip: number of models to skip
        :param limit: max number of models in list
        :returns: list of model objects
        """
        if not custom_filter:
            model_objs = (
                db.query(self.model)
                .order_by(desc(self.model.time_created), desc(self.model.uuid))
                .offset(skip * limit)
                .limit(limit)
                .all()
            )
        else:
            query = db.query(self.model)
            if custom_filter.uuid:
                query = query.filter(self.model.uuid == custom_filter.uuid)
            if custom_filter.name:
                query = query.filter(self.model.name == custom_filter.name)
            if custom_filter.manufacturer_name:
                manufacturer = crud.manufacturer.get(db=db, get_value=custom_filter.manufacturer_name, get_property="name")
                query = query.filter(self.model.manufacturer_uuid == manufacturer.uuid)
            if custom_filter.lens_mount_name:
                lens_mount = crud.lens_mount.get(db=db, get_value=custom_filter.lens_mount_name , get_property="name")
                query = query.filter(self.model.lens_mount_uuid == lens_mount.uuid)
            if custom_filter.min_focal_length:
                query = query.filter(self.model.min_focal_length >= custom_filter.min_focal_length)
            if custom_filter.max_focal_length:
                query = query.filter(self.model.max_focal_length <= custom_filter.max_focal_length)
            if custom_filter.min_aperture:
                query = query.filter(self.model.min_aperture >= custom_filter.min_aperture)
            if custom_filter.max_aperture:
                query = query.filter(self.model.max_aperture <= custom_filter.max_aperture)
            if custom_filter.auto:
                query = query.filter(self.model.auto <= custom_filter.auto)
            if custom_filter.manual:
                query = query.filter(self.model.manual <= custom_filter.manual)

            model_objs = query.order_by(desc(self.model.time_created), desc(self.model.uuid)).offset(skip * limit).limit(limit).all()

        return model_objs


class CRUDLensMount(CRUDBase[LensMount, LensMountCreate, LensMountUpdate]):
    """LensMount crud."""

    pass


lens = CRUDLens(Lens)

lens_mount = CRUDLensMount(LensMount)
