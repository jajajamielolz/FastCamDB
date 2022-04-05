"""Review endpoints."""
from typing import Any
from typing import List
from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request

from app import schemas
from app.api.dependencies.collections import BaseDependencies
from app.services import crud


router = APIRouter(prefix="/reviews", tags=["reviews"], dependencies=BaseDependencies())
router_review_type = APIRouter(
    prefix="/review-type", tags=["review-type"], dependencies=BaseDependencies()
)

# ==== review ====


@router.post("", response_model=schemas.Review)
def create_review(request: Request, body: schemas.ReviewCreate) -> Any:
    """Create a review."""
    return crud.review.create(
        db=request.state.db,
        obj_in=body,
    )


@router.get("/{uuid}", response_model=schemas.Review)
def read_review(
    request: Request,
    uuid: str,
) -> Any:
    """Get a review."""
    return crud.review.get(db=request.state.db, uuid=uuid)


@router.get("", response_model=List[schemas.Review])
def read_reviews(
    request: Request,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """Get a list of reviews."""
    return crud.review.get_multi(
        db=request.state.db,
        skip=skip,
        limit=limit,
    )


@router.patch("/{uuid}", response_model=schemas.Review)
def update_review(request: Request, uuid: str, body: schemas.ReviewUpdate) -> Any:
    """Update a review."""
    return crud.review.update(db=request.state.db, uuid=uuid, obj_in=body)


@router.delete("/{uuid}")
def remove_review(request: Request, uuid: str) -> Any:
    """Remove a review."""
    return crud.review.remove(db=request.state.db, uuid=uuid)

