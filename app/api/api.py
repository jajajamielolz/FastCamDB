"""Ransom endpoint."""
from fastapi import APIRouter

from .endpoints import cameras
from .endpoints import reviews
from .endpoints import tests
from .endpoints import vitals


router = APIRouter()

router.include_router(vitals.router)
router.include_router(cameras.router)
router.include_router(reviews.router)
router.include_router(reviews.router_review_type)
router.include_router(tests.router)
