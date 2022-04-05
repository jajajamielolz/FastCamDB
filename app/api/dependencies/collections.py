"""Dependency collections."""
from fastapi import Depends

from app.api.dependencies.database import attach_user_db


def BaseDependencies():  # noqa
    """Base dependencies for api routes."""
    dependency_list = [
        Depends(attach_user_db),
    ]
    return dependency_list

