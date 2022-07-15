"""Camera endpoints."""
from typing import Any
from typing import List

from fastapi import APIRouter
from fastapi import Request

from app import schemas
from app.api.dependencies.collections import BaseDependencies
from app.services import crud
from fastapi import Depends


router = APIRouter(prefix="/cameras", tags=["cameras"], dependencies=BaseDependencies())


@router.post("", response_model=schemas.Camera)
def create_camera(request: Request, body: schemas.CameraCreate) -> Any:
    """Create an camera."""
    return crud.camera.create_camera(db=request.state.db, obj_in=body)


@router.get("", response_model=List[schemas.Camera])
def read_cameras(
    request: Request,
    skip: int = 0,
    limit: int = 100,
    custom_filter: schemas.CameraFilter = Depends(),
) -> Any:
    """Get a list of cameras."""

    return crud.camera.filter_camera(db=request.state.db, skip=skip, limit=limit, custom_filter=custom_filter)


@router.patch("/{uuid}", response_model=schemas.Camera)
def patch_camera(request: Request, uuid: str, body: schemas.CameraUpdate) -> Any:
    """Update an camera."""
    return crud.camera.update(db=request.state.db, uuid=uuid, obj_in=body)


@router.delete("/{uuid}")
def remove_camera(request: Request, uuid: str) -> Any:
    """Remove a lens."""
    return crud.camera.remove(db=request.state.db, uuid=uuid)