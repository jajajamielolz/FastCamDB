"""App test endpoints."""
from time import sleep

from fastapi import APIRouter
from fastapi import Request
from fastapi_cache.decorator import cache

from app.api.dependencies.collections import BaseDependencies
from app.core.config import config
from app.db.session import get_super_session
from app.db.session import get_user_session

router = APIRouter(prefix="/tests", tags=["tests"])


@router.get("/db/super")
async def db_check_super():
    """Check db connection."""
    db = await get_super_session()
    db.execute('SET SESSION "user.permissions" = :permissions', {"permissions": "test"})
    db.close()
    return f"Database connection to {config.DB_DATABASE} as {config.DB_SUPERUSER} successful"


@router.get("/db/appuser")
async def db_check_user():
    """Check db user."""
    db = await get_user_session()
    db.execute('SET SESSION "user.permissions" = :permissions', {"permissions": "test"})
    db.close()
    return f"Database connection to {config.DB_USERUSER} as successful"


@router.get("/error")
async def error_check(request: Request):
    """Throw error to checking handling/logging."""
    return 1 / 0


@router.get("/cache-check")
@cache(expire=5)
async def check_cache():
    """Checks caching with sleep function."""
    sleep(5)
    return {"message": "If not cached response take at least 5 seconds"}
