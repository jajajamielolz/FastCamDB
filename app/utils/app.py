"""App utilities."""

from app.db import session


def configure_db_connection():
    """Starts up database connections and session makers."""
    session.open_user_connection_pool()
    session.open_super_connection_pool()
    session.set_user_sessionmaker()
    session.set_super_sessionmaker()


def close_database_pool():
    """Closes all active database sessions and disposes of connection pool."""
    session.close_all_user_sessions()
    session.close_all_super_sessions()
    session.close_user_connection_pool()
    session.close_super_connection_pool()
