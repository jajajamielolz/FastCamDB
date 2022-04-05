"""App creation."""
import datetime
import subprocess
import time

from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette_context import plugins
from starlette_context.middleware import ContextMiddleware

from app.api import api
from app.middlewares import exception_catcher


def get_git_revision_hash():
    """Return git revision hash."""
    return subprocess.check_output(["git", "rev-parse", "HEAD"]).strip().decode()


def create_app() -> FastAPI:
    """Build and return FastApi application."""
    # sentry-sdk

    middleware = [
        Middleware(
            ContextMiddleware,
            plugins=(plugins.RequestIdPlugin(), plugins.CorrelationIdPlugin()),
        ),
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_credentials=True,
            allow_headers=["*"],
        ),
    ]

    app = FastAPI(middleware=middleware)

    # middleware
    app.middleware("http")(exception_catcher)

    start_time = time.time()

    def get_uptime():
        conversion = datetime.timedelta(seconds=time.time() - start_time)
        return {"seconds": time.time() - start_time, "HH:MM:SS": str(conversion)}

    # environment.add_section("app uptime", get_uptime)

    app.include_router(api.router)

    return app
