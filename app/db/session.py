"""DB sessions."""
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from app.core.config import config


_user_engine: Optional[Engine]
_super_engine: Optional[Engine]
_user_sessionmaker: Optional[sessionmaker]
_super_sessionmaker: Optional[sessionmaker]


_user_conn_str = (
    f"{config.DB_CONN_METHOD}://{config.DB_USER}:{config.DB_USERPASSWORD}@"
    f"{config.DB_HOSTNAME}/{config.DB_DATABASE}"
)
_super_conn_str = (
    f"{config.DB_CONN_METHOD}://{config.DB_SUPERUSER}:{config.DB_SUPERPASSWORD}@"
    f"{config.DB_HOSTNAME}/{config.DB_DATABASE}"
)


def open_user_connection_pool():
    """Opens and sets a user connection engine."""
    global _user_engine
    _user_engine = create_engine(_user_conn_str, echo=config.ENGINE_ECHO)


def open_super_connection_pool():
    """Opens and sets a super connection engine."""
    global _super_engine
    _super_engine = create_engine(_super_conn_str, echo=config.ENGINE_ECHO)


def close_user_connection_pool():
    """Disposes user connection engine."""
    global _user_engine
    _user_engine.dispose()


def close_super_connection_pool():
    """Disposes super connection engine."""
    global _super_engine
    _super_engine.dispose()


def close_all_user_sessions():
    """Closes all user sessions."""
    global _user_sessionmaker
    _user_sessionmaker.close_all()


def close_all_super_sessions():
    """Closes all super sessions."""
    global _super_sessionmaker
    _super_sessionmaker.close_all()


def set_user_sessionmaker():
    """Opens and sets a user sessionmaker."""
    global _user_sessionmaker
    global _user_engine
    assert _user_engine is not None
    _user_sessionmaker = sessionmaker(
        autoflush=False, autocommit=False, bind=_user_engine
    )


def set_super_sessionmaker():
    """Opens and sets a super sessionmaker."""
    global _super_sessionmaker
    global _super_engine
    assert _super_engine is not None
    _super_sessionmaker = sessionmaker(
        autoflush=False, autocommit=False, bind=_super_engine
    )


def get_user_session() -> Session:
    """Get user session."""
    global _user_sessionmaker
    assert _user_sessionmaker is not None
    return _user_sessionmaker()


def get_super_session() -> Session:
    """Get super session."""
    global _super_sessionmaker
    assert _super_sessionmaker is not None
    return _super_sessionmaker()
