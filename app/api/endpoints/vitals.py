"""App vital endpoints."""
from fastapi import APIRouter
from app import __version__


router = APIRouter(tags=["vitals"])


@router.get("/")
async def welcome():
    """Welcome endpoint."""
    return f"Welcome! You're interacting with FastCamDB@{__version__}"
