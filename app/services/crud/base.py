"""Base CRUD module for all crud operations."""
import datetime
from typing import Any
from typing import Dict
from typing import Generic
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

from fastapi.encoders import jsonable_encoder
from psycopg2.errors import InsufficientPrivilege  # noqa
from pydantic import BaseModel
from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.core import errors
from app.models import DeclarativeBase

ModelType = TypeVar("ModelType", bound=DeclarativeBase)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """CRUD object with default methods to Create, Read, Update, Delete (CRUD)."""

    def __init__(self, model: Type[ModelType]):
        """Init crud base for given model."""
        self.model = model

    def get(
        self,
        db: Session,
        uuid: str,
    ) -> ModelType:
        """
        Get model object of uuid.

        :param db: a db session
        :param uuid: the uuid of the model
        :returns: model object
        """
        model_obj = db.query(self.model).filter(self.model.uuid == uuid).first()
        # record not found
        if model_obj is None:
            raise errors.RecordNotFoundError(model_name=self.model.__name__, uuid=uuid)
        return model_obj

    def get_multi(
        self,
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> List[ModelType]:
        """
        Get a list of model objects.

        :param db: a db session
        :param skip: number of models to skip
        :param limit: max number of models in list
        :returns: list of model objects
        """
        model_objs = (
            db.query(self.model)
            .order_by(desc(self.model.time_created), desc(self.model.uuid))
            .offset(skip * limit)
            .limit(limit)
            .all()
        )

        return model_objs

    def create(
        self,
        db: Session,
        *,
        obj_in: Union[CreateSchemaType, Dict[str, Any]],
    ) -> ModelType:
        """
        Create a model object and commit to db.

        :param db: a db session
        :param obj_in: input model schema object
        :returns: model object
        """
        obj_in_data = jsonable_encoder(obj_in)
        obj_in_data = extract_object_data(obj_in_data, self.model)
        db_obj = self.model(**obj_in_data)  # type: ignore

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        uuid: str,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> ModelType:
        """
        Update a model object.

        :param db: a db session
        :param uuid: uuid of model object
        :param obj_in: a schema object/dict of updated fields
        :returns: model object
        """
        db_obj = self.get(db=db, uuid=uuid)
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        db_obj.time_updated = datetime.datetime.now()

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, uuid: str, commit=True) -> ModelType:
        """
        Remove a model object.

        :param db: a db session
        :param uuid: uuid of model object
        :returns: model object
        """
        obj = db.query(self.model).filter(self.model.uuid == uuid).first()
        if obj is None:
            raise errors.RecordNotFoundError(model_name=self.model.__name__, uuid=uuid)
        db.delete(obj)
        if commit:
            db.commit()
        return obj


def extract_object_data(obj_in_data, model):
    """
    Extract all relevant key value pairs from a dictionary for a model.

    :param obj_in_data: data to extract
    :param model: model class
    """
    obj_cols = [col.name for col in model.__mapper__.columns]
    out_data = {}
    for k, v in obj_in_data.items():
        if k in obj_cols:
            out_data[k] = v
    return out_data
