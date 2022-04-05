"""Data and Model Utilities."""
from typing import Any
from typing import Dict
from typing import List
from typing import Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from app.models.core.base import DeclarativeBase


def create_model_from_data(
    obj_in: Union[BaseModel, Dict[str, Any]],
    model: DeclarativeBase,
    added_data: Dict[str, Any],
):
    """
    Creates an instance of a model using provided data dict/schema.

    :param obj_in: data to build model with
    :param model: model class
    :param added_data: Additional data dictionary to add
    """
    obj_in_data = jsonable_encoder(obj_in)
    obj_in_data = {**obj_in_data, **added_data}
    obj_in_data = filter_to_model_kwargs(obj_in_data, model)
    return model(**obj_in_data)


def filter_to_model_kwargs(obj_in_data, model):
    """
    Filters all relevant key value pairs from a dictionary for a models kwargs.

    :param obj_in_data: data to extract
    :param model: model class
    """
    obj_cols = [col.name for col in model.__mapper__.columns]
    out_data = {}
    for k, v in obj_in_data.items():
        if k in obj_cols:
            out_data[k] = v
    return out_data


def get_model_attr_names(model: DeclarativeBase) -> List[str]:
    """Gets a list of model attribute names."""
    return [
        attr
        for attr in dir(model)
        if not callable(getattr(model, attr)) and not attr.startswith("__")
    ]
