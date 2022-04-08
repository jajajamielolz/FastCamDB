"""Lens endpoints."""
from typing import Any
from typing import List

from fastapi import APIRouter
from fastapi import Request

from app import schemas
from app.api.dependencies.collections import BaseDependencies
from app.services import crud


router = APIRouter(prefix="/lenses", tags=["lenses"], dependencies=BaseDependencies())


@router.post("", response_model=schemas.Lens)
def create_lens(request: Request, body: schemas.LensCreate) -> Any:
    """Create a lens."""
    return crud.lens.create(db=request.state.db, obj_in=body)


@router.get("/{uuid}", response_model=schemas.Lens)
def read_lens(request: Request, uuid: str) -> Any:
    """Get a lens."""
    return crud.lens.get(db=request.state.db, uuid=uuid)


@router.get("", response_model=List[schemas.Lens])
def read_lenses(
    request: Request,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """Get a list of lenses."""
    return crud.lens.get_multi(db=request.state.db, skip=skip, limit=limit)


@router.patch("/{uuid}", response_model=schemas.Lens)
def patch_lens(request: Request, uuid: str, body: schemas.LensUpdate) -> Any:
    """Update an lens."""
    return crud.lens.update(db=request.state.db, uuid=uuid, obj_in=body)
