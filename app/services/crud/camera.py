"""Camera CRUD."""
from app.models import Camera
from app.schemas import CameraCreate
from app.schemas import CameraUpdate
from app.services.crud.base import CRUDBase
from sqlalchemy.orm import Session
from app.services import crud
from app import schemas
from sqlalchemy import desc


class CRUDCamera(CRUDBase[Camera, CameraCreate, CameraUpdate]):
    """Camera crud."""
    def create_camera(self, obj_in: CameraCreate, db: Session) -> Camera:
        """Create a camera."""
        camera_obj = self.create(obj_in=obj_in, db=db)
        # TODO: add change these creates to get or creates from name property
        if obj_in.manufacturer:
            manufacturer = crud.manufacturer.get_or_create(db=db, obj_in=obj_in.manufacturer)
            camera_obj.manufacturer_uuid = manufacturer.uuid
        if obj_in.lens_mount:
            lens_mount = crud.lens_mount.get_or_create(db=db, obj_in=obj_in.lens_mount)
            camera_obj.lens_mount_uuid = lens_mount.uuid
        if obj_in.metering:
            metering = crud.metering.get_or_create(db=db, obj_in=obj_in.metering)
            camera_obj.metering_uuid = metering.uuid
        db.commit()
        return camera_obj

    def filter_camera(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 100,
        custom_filter: schemas.CameraFilter = None,
    ) -> Camera:
        """
        Get a list of model objects.

        :param custom_filter: parameters to filter cameras
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
                manufacturer = crud.manufacturer.get_or_create(db=db, obj_in=schemas.ManufacturerCreate(name=custom_filter.manufacturer_name))
                query = query.filter(self.model.manufacturer_uuid == manufacturer.uuid)
            if custom_filter.lens_mount_name:
                lens_mount = crud.lens_mount.get_or_create(db=db, obj_in=schemas.LensMountCreate(name=custom_filter.lens_mount_name))
                query = query.filter(self.model.lens_mount_uuid == lens_mount.uuid)
            if custom_filter.metering_name:
                metering = crud.metering.get_or_create(db=db, obj_in=schemas.MeteringCreate(name=custom_filter.metering_name))
                query = query.filter(self.model.metering_uuid == metering.uuid)
            model_objs = query.order_by(desc(self.model.time_created), desc(self.model.uuid)).offset(skip * limit).limit(limit).all()

        return model_objs


camera = CRUDCamera(Camera)
