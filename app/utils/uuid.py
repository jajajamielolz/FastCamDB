"""UUID utils."""
import uuid


def generate_uuid_str() -> str:
    """Return a generated uuid ID string."""
    return str(uuid.uuid4())


def generate_uuid() -> uuid.UUID:
    """Return a generated uuid ID string."""
    return uuid.uuid4()
