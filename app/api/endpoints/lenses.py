"""Lens endpoints."""
from typing import Any
from typing import List

from fastapi import APIRouter
from fastapi import Request

from app import schemas
from app.api.dependencies.collections import BaseDependencies
from app.services import crud
from fastapi import Depends


router = APIRouter(prefix="/lenses", tags=["lenses"], dependencies=BaseDependencies())


@router.post("", response_model=schemas.Lens)
def create_lens(request: Request, body: schemas.LensCreate) -> Any:
    """Create a lens."""
    return crud.lens.create_lens(db=request.state.db, obj_in=body)


@router.get("", response_model=List[schemas.Lens])
def read_lenses(
    request: Request,
    skip: int = 0,
    limit: int = 100,
    custom_filter: schemas.LensFilter = Depends(),

) -> Any:
    """Get a list of lenses."""
    return crud.lens.filter_lens(db=request.state.db, skip=skip, limit=limit, custom_filter=custom_filter)


@router.patch("/{uuid}", response_model=schemas.Lens)
def patch_lens(request: Request, uuid: str, body: schemas.LensUpdate) -> Any:
    """Update an lens."""
    return crud.lens.update(db=request.state.db, uuid=uuid, obj_in=body)


@router.delete("/{uuid}")
def remove_lens(request: Request, uuid: str) -> Any:
    """Remove a lens."""
    return crud.lens.remove(db=request.state.db, uuid=uuid)