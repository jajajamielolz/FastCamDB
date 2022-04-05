"""App configuration."""
import os
from typing import Optional

from pydantic import BaseSettings

from app.core import errors


ENV = os.environ.get("ENVIRONMENT")


class GlobalConfig(BaseSettings):
    """Global configuration."""

    ENVIRONMENT: str

    # Server
    SERVER_HOST: Optional[str] = "0.0.0.0"
    SERVER_PORT: Optional[int] = 8000

    # DB
    DB_DATABASE: str
    DB_HOSTNAME: str
    DB_TYPE: str
    DB_CONN_METHOD: str
    POOL_SIZE: int
    MAX_OVERFLOW: int

    # DB Users
    DB_SUPERUSER: str
    DB_SUPERPASSWORD: str
    DB_USERUSER: str
    DB_USERPASSWORD: str

    # Echo sql
    ENGINE_ECHO: bool = False

    class Config:
        env_file: str = ".env"


class DevConfig(GlobalConfig):
    """Development configuration."""

    class Config:
        env_file: str = ".env.development"


class ProdConfig(GlobalConfig):
    """Production configuration."""

    class Config:
        env_file: str = ".env.production"


class StageConfig(GlobalConfig):
    """Staging configuration."""

    class Config:
        env_file: str = ".env.staging"


class TestConfig(GlobalConfig):
    """Testing configuration."""

    class Config:
        env_file: str = ".env.testing"


class LocalConfig(GlobalConfig):
    """Local Container configuration."""

    class Config:
        env_file: str = ".env.local"


class FactoryConfig:
    """Returns config instance based on environment variable."""

    def __init__(self, environment: Optional[str] = "development"):
        """Init factory."""
        self.environment = environment

    def __call__(self):
        """Return config based on environment."""
        if self.environment == "development":
            return DevConfig()
        if self.environment == "staging":
            return StageConfig()
        if self.environment == "production":
            return ProdConfig()
        if self.environment == "testing":
            return TestConfig()
        if self.environment == "local":
            return LocalConfig()
        else:
            raise errors.InvalidEnvironment(environment=self.environment)


config: GlobalConfig = FactoryConfig(environment=ENV)()
