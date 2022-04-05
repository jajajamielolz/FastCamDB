"""Main file, runs service."""
import datetime
import logging

import uvicorn
from uvicorn.supervisors import ChangeReload
from uvicorn.supervisors import Multiprocess

from app.core.config import config
from app.core.create import create_app  # noqa
from app.utils import app as app_utils

START_TIME = datetime.datetime.now()
UVICORN_LOGGING_MODULES = ("uvicorn.error", "uvicorn.asgi", "uvicorn.access")

app = create_app()


# === Startup Hooks ====


@app.on_event("startup")
def startup():
    """Starts up database connections and session makers."""
    app_utils.configure_db_connection()


# ==== Shutdown Hooks ====


@app.on_event("shutdown")
def shutdown():
    """Closes all active database sessions and disposes of connection pool."""
    app_utils.close_database_pool()


def run_uvicorn():
    """Run uvicorn server with app."""
    uv_config = uvicorn.Config(
        app,
        host=config.SERVER_HOST,
        port=config.SERVER_PORT,
        log_level="info",
        reload=True,
    )
    server = uvicorn.Server(config=uv_config)
    supervisor_type = None
    if uv_config.should_reload:
        supervisor_type = ChangeReload
    if uv_config.workers > 1:
        supervisor_type = Multiprocess
    if supervisor_type:
        sock = uv_config.bind_socket()
        supervisor = supervisor_type(uv_config, target=server.run, sockets=[sock])
        supervisor.run()
    else:
        server.run()


def main():
    """Main function."""
    run_uvicorn()


if __name__ == "__main__":
    main()
