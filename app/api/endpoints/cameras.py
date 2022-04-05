"""Camera endpoints."""
from typing import Any
from typing import List

from fastapi import APIRouter
from fastapi import Request

from app import schemas
from app.api.dependencies.collections import BaseDependencies
from app.services import crud


router = APIRouter(prefix="/cameras", tags=["cameras"], dependencies=BaseDependencies())


@router.post("", response_model=schemas.Camera)
def create_camera(request: Request, body: schemas.CameraCreate) -> Any:
    """Create an camera."""
    return crud.camera.create(db=request.state.db, obj_in=body)


@router.get("/{uuid}", response_model=schemas.Camera)
def read_camera(request: Request, uuid: str) -> Any:
    """Get an camera."""
    return crud.camera.get(db=request.state.db, uuid=uuid)


@router.get("", response_model=List[schemas.Camera])
def read_cameras(
    request: Request,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """Get a list of cameras."""
    cameras_page = crud.camera.get_multi(db=request.state.db, skip=skip, limit=limit)

    return cameras_page


@router.patch("/{uuid}", response_model=schemas.Camera)
def patch_camera(request: Request, uuid: str, body: schemas.CameraUpdate) -> Any:
    """Update an camera."""
    return crud.camera.update(db=request.state.db, uuid=uuid, obj_in=body)
