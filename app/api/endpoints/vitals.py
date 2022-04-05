"""App vital endpoints."""
from fastapi import APIRouter
from fastapi import Request

from app import __version__
from app.api.dependencies.collections import BaseDependencies


router = APIRouter(tags=["vitals"])


@router.get("/")
async def welcome():
    """Welcome endpoint."""
    return f"Welcome! You're interacting with TBD@{__version__}"


@router.get("/me", dependencies=BaseDependencies())
async def user_check(request: Request):
    """Check current user."""
    return f"Connected as user: {request.state.user_id}"


@router.get("/uptime")
async def get_uptime(request: Request):
    """Get server runtime."""
    pass
