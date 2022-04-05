"""Database dependency."""
from typing import AsyncIterable

from fastapi import Depends
from fastapi import Request
from sqlalchemy.orm import Session

from app.db.session import get_super_session
from app.db.session import get_user_session


async def get_user_db(db=Depends(get_user_session)) -> AsyncIterable[Session]:
    """Yield a db session for user."""
    try:
        yield db
    finally:
        db.close()


async def get_super_db(db=Depends(get_super_session)) -> AsyncIterable[Session]:
    """Yield a db super session."""
    try:
        yield db
    finally:
        db.close()


def attach_user_db(request: Request, db: Session = Depends(get_user_db)):
    """Attach db session of user to request."""
    request.state.db = db


def attach_super_db(request: Request, db: Session = Depends(get_super_db)):
    """Attache a super db session to request."""
    request.state.db = db
