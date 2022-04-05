"""Review CRUD."""
from app.models import Review
from app.schemas import ReviewCreate
from app.schemas import ReviewUpdate
from app.services.crud.base import CRUDBase


class CRUDReview(CRUDBase[Review, ReviewCreate, ReviewUpdate]):
    """Review crud."""

    pass


review = CRUDReview(Review)

